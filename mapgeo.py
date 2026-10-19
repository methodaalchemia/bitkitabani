"""Kültür köprüleri haritası: Natural Earth I izdüşümü (kamu malı Natural Earth 1:110m kara verisi)."""
import math, os
HERE = os.path.dirname(os.path.abspath(__file__))
W = 1000
LAT_MIN, LAT_MAX = -58, 78

def _raw(lon, lat):
    l, p = math.radians(lon), math.radians(lat)
    p2 = p * p; p4 = p2 * p2
    x = l * (0.8707 - 0.131979 * p2 + p4 * (-0.013791 + p4 * (0.003971 * p2 - 0.001529 * p4)))
    y = p * (1.007226 + p2 * (0.015085 + p4 * (-0.044475 + 0.028874 * p2 - 0.005916 * p4)))
    return x, y

XMAX = _raw(180, 0)[0]
YTOP, YBOT = _raw(0, LAT_MAX)[1], _raw(0, LAT_MIN)[1]
S = W / (2 * XMAX)
H = round((YTOP - YBOT) * S)

def project(lon, lat):
    x, y = _raw(lon, lat)
    return round((x + XMAX) * S, 1), round((YTOP - y) * S, 1)

def land_path():
    return open(os.path.join(HERE, 'map_land.txt'), encoding='utf-8').read().strip()

if __name__ == '__main__':
    import json, sys
    g = json.load(open(sys.argv[1]))
    parts = []
    for f in g['features']:
        geom = f['geometry']
        polys = geom['coordinates'] if geom['type'] == 'MultiPolygon' else [geom['coordinates']]
        for poly in polys:
            for ring in poly:
                if max(pt[1] for pt in ring) < LAT_MIN: continue  # Antarktika
                pts, last = [], None
                for lon, lat in ring:
                    lat = max(min(lat, LAT_MAX), LAT_MIN)
                    q = project(lon, lat); q = (round(q[0]), round(q[1]))
                    if q != last: pts.append(q); last = q
                if len(pts) < 4: continue
                parts.append('M' + 'L'.join(f'{x} {y}' for x, y in pts) + 'Z')
    open(os.path.join(HERE, 'map_land.txt'), 'w').write(''.join(parts))
    print('kara yolu', len(''.join(parts)), 'karakter; boyut', W, 'x', H)
