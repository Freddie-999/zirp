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

def read_coord():
    """load coordniates from user input"""
    poi = gpd.read_file('coordinates.json')
    print(poi.shape)

read_coord()