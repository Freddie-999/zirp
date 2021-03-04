import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json


country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')

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
    """read the of country and towns""" #TOdo towns
    country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')
    countryboundary_projected = country.to_crs(epsg=3857)
    return countryboundary_projected
mydistrict = read_shape_file()


plt.rcParams['figure.figsize'] = [10, 10] #this sets the size of the figure

fig, myax = plt.subplots()
mydistrict.plot(ax=myax, color='red', ec='gray', alpha=0.2)
mypoint.plot(ax=myax, color='blue')

def add_basemap():
    print("Drawing map, please wait...")
    src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ctx.add_basemap(ax=myax, source=src_basemap, alpha=0.6, zorder=8)
    plt.show()
add_basemap() 




def select_dist():
    """select district of interest"""
    pass



def get_nearest_town():
    """find the nearest town to incident"""
    pass



def get_info():
    """return the info for the nearest town"""
    pass



