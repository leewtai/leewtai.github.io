import os

import matplotlib.pyplot as plt
import numpy as np
import rioxarray as rxr
import geopandas as gpd
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

# Download data and set working directory
data = et.data.get_data('cold-springs-fire')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'data'))

naip_data_path = os.path.join(
    "cold-springs-fire",
    "naip",
    "m_3910505_nw_13_1_20150919",
    "crop",
    "m_3910505_nw_13_1_20150919_crop.tif")

naip_data = rxr.open_rasterio(naip_data_path)

# View shape of the data
naip_data.shape

naip_ndvi = es.normalized_diff(naip_data[3], naip_data[0])
