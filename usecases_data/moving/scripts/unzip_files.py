import os
import zipfile

zip_file_path = '../data/taipei_lie_li_shp.zip'
extraction_path = '../data/taipei_lie_li_shp/'

if os.path.exists(extraction_path):
    os.makedirs(extraction_path)

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)
