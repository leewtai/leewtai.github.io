from glob import glob
from pathlib import Path
import tarfile

import pandas as pd

gz_files = glob('*.gz')
ungz_folder = Path('unzipped_ushcn')
ungz_folder.mkdir(exist_ok=True)

# Each zip corresponds to one type of weather variable,
# Each zip has a folder named after the date of download
# then each folder has multiple raw text files inside that
# correspond to different stations.
for gf in gz_files:
    with tarfile.open(gf, 'r:gz') as gf_tar:
        gf_tar.extractall(ungz_folder.name)

# Raw files follow a format specified in the readme.txt
data_char = {
    'id': (0, 11),
    'year': (12, 16)}
last_char_pos = 16
for month in range(1, 13):
    data_char.update(
        {'value{}'.format(month): (last_char_pos, last_char_pos + 6),
         'dmflag{}'.format(month): (last_char_pos + 6, last_char_pos + 6 + 1),
         'qcflag{}'.format(month): (last_char_pos + 7, last_char_pos + 7 + 1),
         'dsflag{}'.format(month): (last_char_pos + 8, last_char_pos + 8 + 1)})
    last_char_pos += 9


# This loop reads the data into memory and also removes the files/folders
# after it's done. Not optimal given we may run out of memory.
bag = {}
for date_folder in ungz_folder.iterdir():
    for raw_file in dfolder.iterdir():
        # Detect variable
        var = raw_file.suffix[1:]
        if var not in bag:
            bag.update({var: []})
        file_vals = []
        with raw_file.open('r') as rf:
            for line in rf.readlines():
                line_vals = {}
                for dval, pos in data_char.items():
                    val = line[pos[0]:pos[1]]
                    if dval.startswith('value') or dval == 'year':
                        val = int(val)
                    line_vals.update({dval: val})
                file_vals.append(line_vals)
        bag.get(var).extend(file_vals)
        raw_file.unlink()
    dfolder.rmdir()

ungz_folder.rmdir()
Path('csvs').mkdir(exist_ok=True)
for var in bag:
    df = pd.DataFrame(bag.get(var))
    df.tocsv("csvs/{}.csv".format(var)


meta_char = {
    'country': (0, 2),
    'id': (0, 11),
    'latitude': (12, 20),
    'longitude': (21, 30),
    'elevation': (32, 37),
    'state': (38, 40),
    'utc_offset': (93, 95)}

stations = []
with open('ushcn-v2.5-stations.txt', 'r') as f:
    station = {}
    for line in f.readlines():
        for var, pos in meta_char.items():
            val = line[pos[0]:pos[1]]
            if var in ['latitude', 'longitude', 'elevation']:
                val = float(val)
            station.update({var: val})
        stations.append(station)

meta = pd.DataFrame(stations).to_csv('csvs/stations_meta.csv')
