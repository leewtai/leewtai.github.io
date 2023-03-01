import gdal
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rasterio
import shapely


# polygons
df = pd.read_csv('data/mayan_language_map.csv')
gdf = gpd.GeoDataFrame(df)
gdf['geometry'] = gdf.geometry.apply(shapely.wkt.loads)
gdf.head(3)
# Verify the polygons
gdf.plot()
plt.savefig('test.png')
plt.close()

geo = gdf.geometry[0]

# target raster
rast = rasterio.open('data/Hansen_GFC-2021-v1.9_lossyear_20N_090W.tif')

# https://stackoverflow.com/questions/47404898/find-indices-of-raster-cells-that-intersect-with-a-polygon
# allTouched means anything touching the polygon will be flagged
ds = gdal.Rasterize('test_rast', gdf.iloc[:1, :].to_json(),
                    xRes=rast.res[0], yRes=rast.res[1],
                    allTouched=True, outputBounds=rast.bounds,
                    burnValues=1, outputType=gdal.GDT_Byte)
mask = ds.ReadAsArray()
ds = None
gdal.Unlink('test_rast')

# This is just to check stuff, very slow!
# plt.imshow(mask)
# plt.savefig('mask.png')
# plt.close()
y_ind, x_ind = np.where(mask == 1)

forestloss = rast.read(1)
vals = forestloss[y_ind, x_ind]

