from glob import glob
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

files = glob('*json')
data = [json.load(open(f, "r")) for f in files]

feats = data[0]['features']
df = pd.DataFrame(
    [{'long': ft['geometry']['coordinates'][0],
      'lat': ft['geometry']['coordinates'][1],
      'time': ft['properties']['time_long']}
     for ft in feats])

# The records are not in order because there exist negative time stamps
# if we don't sort the data
df.sort_values(by='time', inplace=True)
np.nanpercentile(df.time.diff(), [1, 99])

i = df.shape[0]
plt.scatter(df.long[:i], df.lat[:i])
plt.scatter(df.long[-10:], df.lat[-10:])
plt.savefig('initial_gps_glimps.png')
plt.close()
# Some data on the way back was lost....not sure why
