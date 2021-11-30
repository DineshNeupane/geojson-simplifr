import json
import geometry

with open('bhajani.geojson') as f:
    # feature collection
    fc = json.load(f)


def simplifyFeature(feat, tolerence):
    geom = feat['geometry']
    type = geom['type']

    if type == 'Linestring':
        geom['coordinates'] = geometry.simplifyGeometry(geom['coordinates'], tolerence)
    elif type == 'Polygon' or type == 'MultiLineString':
        for j in range(0, len(geom['coordinates'])):
            geom['coordinates'][j] = geometry.simplifyGeometry(geom['coordinates'][j], tolerence)
    elif type == 'MultiPolygon':
        for k in range(0, len(geom['coordinates'])):
            for l in range(0, len(geom['coordinates'])):
                print("sfe 7")
                geom['coordinates'][k][l] = geometry.simplifyGeometry(geom['coordinates'][k][l], tolerence)
                print("sfe 6")

    return feat


def simplify(fc, tolerance):
    for i in range(0, len(fc['features'])):
        fc['features'][i] = simplifyFeature(fc['features'][i], tolerance)
    new_f = open("geojson_simplified.geojson", "w+")
    json.dump(fc, new_f)
    f.close()




simplify(fc, 0.001)
