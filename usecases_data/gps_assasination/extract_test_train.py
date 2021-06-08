import json
from pathlib import Path
from glob import glob

import numpy as np

# Give example test dataset: first time stamp is leaving the house
# 2nd time stamp is the starting point of the return trip, assumed
# to be the time point after the largest time gap
test_files = glob('./cln_data/202009*.geojson')

for test_file in test_files:
    geo_file = Path(test_file)
    gps = json.load(geo_file.open('r'))
    times = [feat['properties']['time_long'] for feat in gps['features']]
    diff_time = np.diff(times)
    max_ind = np.argmax(diff_time)
    gps_sub = gps
    gps_sub['features'] = [gps_sub['features'][0], gps_sub['features'][max_ind + 1]]
    print(type(gps_sub['features']))
    print(len(gps_sub['features']))
    json.dump(gps_sub,
              open('./test_train_data/{}'.format(geo_file.name),
                   'w'))
