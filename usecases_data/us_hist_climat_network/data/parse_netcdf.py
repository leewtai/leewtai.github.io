from glob import glob
from netCDF4 import Dataset

netcdf_files = glob('netcdfs/*.nc')
dat = Dataset(netcdf_files[0], 'r', format='NETCDF4')

lons = dat['longitude']
lats = dat['lat']
time = dat['times']
pr = dat['pr'] 
