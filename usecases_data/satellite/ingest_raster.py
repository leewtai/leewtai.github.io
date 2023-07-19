# https://rasterio.readthedocs.io/en/latest/quickstart.html
import rasterio
import numpy as np

# Data from https://storage.googleapis.com/earthenginepartners-hansen/GFC-2021-v1.9/download.html
# Get the `lossyear` file
rast = rasterio.open('/Users/waynetailee/Downloads/Hansen_GFC-2021-v1.9_lossyear_20N_090W.tif')

# The extent of the data
rast.bounds
# Coordinate reference system CRS tells you how data is projected
rast.crs

rast.shape

# Get first band of data
band1 = rast.read(1)
np.mean(band1 == 0)
np.mean(band1 == 21)
