# -*- coding: utf-8 -*-
"""Köprü videosu — seslendirme, zamanlama ve .srt üretimi.

Cümle cümle seslendirir, her cümlenin süresini ffprobe ile ölçer, araya sabit
sessizlik koyar. Böylece altyazı zamanı tahmin edilmez, ölçülür: Gemini
hizalamasına ve WordBoundary'ye gerek kalmaz.
"""
import asyncio, json, os, subprocess, sys

SES = os.environ.get('KOPRU_SES', 'tr-TR-EmelNeural')
ARA = float(os.environ.get('KOPRU_ARA', '0.38'))       # cümleler arası sessizlik
SAHNE_ARA = float(os.environ.get('KOPRU_SAHNE_ARA', '0.75'))  # sahneler arası


def _sure(yol):
    o = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                        '-of', 'csv=p=0', yol], capture_output=True, text=True, check=True)
    return float(o.stdout.strip())


async def _soyle(metin, yol):
    import edge_tts
    await edge_tts.Communicate(metin, SES).save(yol)


def seslendir(senaryo, klasor):
    """Her cümleyi ayrı mp3 yapar; (sahne, cümle, dosya, süre) listesi döner."""
    os.makedirs(klasor, exist_ok=True)
    parcalar = []
    for si, sahne in enumerate(senaryo['sahneler']):
        for ci, cumle in enumerate(sahne['metin']):
            yol = os.path.join(klasor, f'{si:02d}-{ci:02d}.mp3')
            if not os.path.exists(yol):
                asyncio.run(_soyle(cumle, yol))
            parcalar.append({'sahne': si, 'cumle': cumle, 'yol': yol, 'sure': _sure(yol)})
    return parcalar


def zaman_cizgisi(parcalar, senaryo):
    """Cümlelere başlangıç/bitiş, sahnelere süre yazar."""
    t = 0.0
    son_sahne = None
    for p in parcalar:
        if son_sahne is not None and p['sahne'] != son_sahne:
            t += SAHNE_ARA
        elif son_sahne is not None:
            t += ARA
        p['bas'], p['bit'] = t, t + p['sure']
        t = p['bit']
        son_sahne = p['sahne']
    sahneler = []
    for si, sahne in enumerate(senaryo['sahneler']):
        ps = [p for p in parcalar if p['sahne'] == si]
        bas = ps[0]['bas'] - (SAHNE_ARA / 2 if si else 0)
        bit = ps[-1]['bit'] + (SAHNE_ARA / 2 if si < len(senaryo['sahneler']) - 1 else 0.6)
        sahneler.append({'no': si, 'bolum': sahne['bolum'], 'bas': max(0, bas), 'bit': bit,
                         'sure': bit - max(0, bas)})
    return parcalar, sahneler, t + 0.6


def ses_birlestir(parcalar, senaryo, hedef):
    """Cümleleri sessizliklerle birleştirip tek mp3 yapar."""
    liste = hedef + '.txt'
    sessiz = os.path.join(os.path.dirname(hedef), '_sessiz_%s.mp3')
    for ad, sn in (('ara', ARA), ('sahne', SAHNE_ARA)):
        y = sessiz % ad
        if not os.path.exists(y):
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i',
                            'anullsrc=r=24000:cl=mono', '-t', str(sn), y], check=True)
    with open(liste, 'w', encoding='utf-8') as f:
        son = None
        for p in parcalar:
            if son is not None:
                f.write("file '%s'\n" % (sessiz % ('sahne' if p['sahne'] != son else 'ara')))
            f.write("file '%s'\n" % p['yol'])
            son = p['sahne']
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
                    '-i', liste, '-c:a', 'libmp3lame', '-b:a', '160k', hedef], check=True)
    return hedef


def _ts(x):
    sa, x = int(x // 3600), x % 3600
    dk, sn = int(x // 60), x % 60
    return f'{sa:02d}:{dk:02d}:{sn:06.3f}'.replace('.', ',')


def srt(parcalar, hedef):
    with open(hedef, 'w', encoding='utf-8') as f:
        for i, p in enumerate(parcalar, 1):
            f.write(f'{i}\n{_ts(p["bas"])} --> {_ts(p["bit"])}\n{p["cumle"]}\n\n')
    return hedef


if __name__ == '__main__':
    kok = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    slug = sys.argv[1] if len(sys.argv) > 1 else 'sedef'
    sen = json.load(open(os.path.join(kok, 'tools/kopru_senaryo', slug + '.json'), encoding='utf-8'))
    cik = os.path.join(kok, 'kopru-video', slug)
    os.makedirs(cik, exist_ok=True)
    parcalar = seslendir(sen, os.path.join(cik, 'ses'))
    parcalar, sahneler, toplam = zaman_cizgisi(parcalar, sen)
    ses_birlestir(parcalar, sen, os.path.join(cik, f'{slug}.mp3'))
    srt(parcalar, os.path.join(cik, f'{slug}.tr.srt'))
    json.dump({'ses': SES, 'toplam': toplam, 'sahneler': sahneler,
               'cumleler': [{k: p[k] for k in ('sahne', 'cumle', 'bas', 'bit')} for p in parcalar]},
              open(os.path.join(cik, 'zaman.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(f'ses: {SES}  toplam: {int(toplam//60)}:{toplam%60:05.2f}')
    for s in sahneler:
        print(f"  {s['no']} {s['bolum'][:34]:<34} {s['bas']:6.2f} → {s['bit']:6.2f}  ({s['sure']:5.2f} sn)")
