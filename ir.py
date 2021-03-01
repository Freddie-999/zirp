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
#coordinates = get_coord()
#print(coordinates)
#coordinates.file"coordinates.geojson", driver='GeoJSON')

def coord_file():
    """write coordinates to file"""
    coordinates = get_coord()
    filename = 'coordinates.json'
    with open(filename, 'w') as f:
        json.dump(coordinates, f)
        return coordinates
coord_file()


def read_shape_file():
    """read the of country and towns""" #TOdo towns
    country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')
    print(country.shape)
    #print(country.head())
    #country.plot()
    #plt.show()
read_shape_file()

#convert from on crs to another
country_new = country.to_crs(epsg=3857)
print('web mercator', country_new.crs)



def select_dist():
    """select district of interest"""
    pass



def get_nearest_town():
    """find the nearest town to incident"""
    pass



def get_info():
    """return the info for the nearest town"""
    pass



def add_basemap_():
    """Add a basemap"""
    country_plt = country_new.plot(figsize=(9, 9), zorder=10, ec='gray', alpha=0.25)
    #src_basemap = ctx.providers.Stamen.Terrain
    print("Drawing map, please wait...")
    src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ctx.add_basemap(country_plt, source=src_basemap, alpha=0.6, zorder=8)
    plt.show()
add_basemap_()









