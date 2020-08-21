from glob import glob
import json
import numpy as np
import matplotlib.pyplot as plt
import utm


files = glob('data/*.geojson')
my_loc = json.load(open('my_house.geojson', 'r'))
my_lonlat = my_loc['features'][0]['geometry']['coordinates']
zone = 12
my_utm = utm.from_latlon(my_lonlat[1], my_lonlat[0],
                         force_zone_number=zone)


dist_thresh = 100
for f in files:
    datum = json.load(open(f, 'r'))
    last_time = np.nan
    collection = []
    print('there are {} records'.format(len(datum['features'])))
    for record in datum['features']:
        record_lonlat = record['geometry']['coordinates']
        record_utm = utm.from_latlon(record_lonlat[1], record_lonlat[0],
                                     zone)
        utm_diff = np.array([record_utm[i] - my_utm[i] for i in range(2)])
        if np.sqrt(np.sum(np.power(utm_diff, 2))) <= dist_thresh:
            # print('time is {}'.format(record['properties']['time_long']))
            continue
        collection.append(record)

    print('there are {} records after cleaning'.format(len(collection)))
    datum['features'] = collection
    json.dump(datum, open('cln_{}'.format(f), 'w'))


for f in files[:3]:
    collection = json.load(open('cln_{}'.format(f), 'r'))['features']
    lons = [i['geometry']['coordinates'][0] for i in collection]
    lats = [i['geometry']['coordinates'][1] for i in collection]
    plt.scatter(lons, lats)


# plt.scatter(my_lonlat[0], my_lonlat[1], color='black')
plt.title('GPS Path to School')
plt.ylabel('latitude')
plt.xlabel('longitude')
plt.savefig('initial_gps_glimps.png')
plt.close()
