import json

import geopandas as gpd
import matplotlib.pyplot as plt
import shapely as shp
from shapely.ops import unary_union

wkid = 2273
# According to https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/pdf/projected_coordinate_systems.pdf
# 2273 is "NAD_1983_StatePlane_South_Carolina_FIPS_3900_Feet_Int"

with open("north_charleston_sc_neighbhoods_polygons.json", "r") as f:
    hoods = json.load(f)
k, v = next(iter(hoods.items()))

neighborhoods = []
subdivisions = []
geometries = []
for v in hoods.values():
    spat_ref = v.get("spatialReference")
    if spat_ref:
        assert spat_ref.get("wkid") == wkid
    feats = v.get("features")
    if not feats:
        continue
    for feat in feats:
        geo = []
        for ring in feat.get("geometry").get('rings'):
            poly = shp.geometry.Polygon(ring)
            geo.append(poly)
        geo = unary_union(geo)
        assert geo.geom_type in ["Polygon", "MultiPolygon"], f"Unexpected geometry type: {geo.geom_type}"
        subdivisions.append(feat.get('attributes').get('SUBDIVISION'))
        neighborhoods.append(feat.get('attributes').get('NEIGHBOR'))
        geometries.append(geo)


df = gpd.GeoDataFrame({
    'neighbor': neighborhoods,
    'subdiv': subdivisions,
    'geometry': geometries},
    crs=f"EPSG:{wkid}")
    
df.to_file("north_charleston_neighborhoods",
           index=False)
