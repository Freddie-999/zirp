import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json


def get_coord():
    """get coordinates from user and plot """ 
    while True:
        try:
            x, y = (input("Enter coordinates separated by a ',':\n").split(","))
            return float(x), float(y)
        except ValueError:
            print('check your input')            
coordinates = get_coord()

coordinates_dictionary = {
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": coordinates
  },
  "properties": {
    "name": "last known location"
  }
}
with open('new_coords.geojson', 'w') as f:
    json.dump(coordinates_dictionary, f)


def read_point():
    """read coordinates on a from the saved .json file"""
    point_df = gpd.read_file('new_coords.geojson')
    point_df_new = point_df.to_crs(epsg=3857)
    return point_df_new
mypoint = read_point()



def read_shape_file():
    """read the districts to gpd""" #TOdo towns
    districts = gpd.read_file('/Users/freddie/Downloads/district/GH_DISTRICTS_260.shp')
    districtboundary_projected = districts.to_crs(epsg=3857)
    return districtboundary_projected
mydistrict = read_shape_file()


def read_towns():
    """get coordinates of towns"""
    df = pd.read_csv('/Users/freddie/Downloads/jira_data.csv')
    points = df.apply(lambda row: Point(row.Longitude, row.Latitude), axis=1)
    towns = gpd.GeoDataFrame(df, geometry=points)
    towns.plot()

read_towns()

#spatial analysis
buffer = mypoint['geometry'].buffer(distance = 1200)
buffer_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer))
buffer_df = buffer_df.rename(columns={0:'geometry'}).set_geometry('geometry')
print(buffer_df)
buffer_df.to_file(r"/Users/freddie/test2.shp")

join = gpd.sjoin(mydistrict, buffer_df, how="inner", op="intersects")
print(join)
join.to_file(r"/Users/freddie/test.shp")



#plotting to map
plt.rcParams['figure.figsize'] = [10, 10] #this sets the size of the figure
fig, myax = plt.subplots()
#mydistrict.plot(ax=myax, ec='gray', alpha=0.2, column='Name')
buffer.plot(ax=myax, ec='gray', alpha=0.2, edgecolor='black')
mypoint.plot(ax=myax, color='red')
#join.plot(ax=myax, ec='gray', alpha=0.2, edgecolor='black')
#mytowns.plot(ax=myax, color='green')

def add_basemap():
    print("Drawing map, please wait...")
    src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ctx.add_basemap(ax=myax, source=src_basemap, alpha=0.6, zorder=8)
    plt.show()
add_basemap() 




def get_nearest_town():
    """find the nearest town to incident"""
    pass



def get_info():
    """return the info for the nearest town"""
    pass



