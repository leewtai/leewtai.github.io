import geopandas as gpd

hoods = gpd.read_file('../data/taipei_lie_li_shp/G97_A_CALIN_P.shp')

hoods.shape
hoods.iloc[0]
