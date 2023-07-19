import os

import autocensus
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely as shp
from shapely.ops import unary_union


# Create a Census object
census_key = os.getenv("CENSUS_KEY")
hoods = gpd.read_file("north_charleston_neighborhoods")
# Match census projection
hoods.to_crs(epsg=4269, inplace=True)
# Areas are only used for ratio calculation
hoods['neighbor_area'] = hoods.area
hoods.head(3)

# Define the range of years we want
years = list(range(2020, 2022))

# Define the variable we want to analyze
table = "B19001"
vars = [f'{table}_{col:03}{v}'
        for col in range(1, 18) # 1 to 18 yields [1, ..., 17]
        for v in ['E']] # E = estimate, M = margin of error
print(vars)

# Query the data from census.gov via autocensus.Query()
query = autocensus.Query(
    estimate=5,  # this specifies whether you want the 1, 3, or 5 year ACS estimates
    years=years, # since we looked up the 2021 documentation
    variables=vars,
    for_geo=['tract:*'],
    in_geo=['state:45', 'county:019'], # SC 45, Charleston: 019
    geometry='polygons',
    census_api_key=census_key
)
census = query.run()
census.head(3)
census = gpd.GeoDataFrame(census, geometry=census.geometry)
census.columns
census.drop(columns=['geo_id', 'geo_type', 'annotation', 'variable_concept'], inplace=True)
# A few tracts have None as their geometry
census['census_geo'] = census.geometry.apply(lambda x: unary_union(x) if x else None)


geom_type = census.census_geo.apply(lambda x: x.geom_type if x else None)
demo = census[geom_type == 'MultiPolygon'].iloc[:1, :]
demo.plot()
plt.show()

df = hoods.sjoin(census, how='left')
df.shape
hoods.shape
census.shape
df.columns


def frac_area_to_neighborhood(x):
    if x['census_geo'] is None:
        return 0
    return x['census_geo'].intersection(x['geometry']).area / x['geometry'].area

df['area_ratio'] = df.apply(frac_area_to_neighborhood, axis=1)
df.area_ratio.describe()

plt.hist(df.area_ratio)
plt.show()

big_overlap = df.area_ratio > 0.8 
sdf = df[big_overlap]
sdf.shape
hoods.shape
census.shape

sdf.groupby(["neighbor", "subdiv"]).size()
# The duplicates are due to the different metrics
# over years. The location is the same!

sdf.to_csv("north_charleston_neighborhoods_census.csv", index=False)