import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json

#set paths for shapefiles
towns = '/Users/freddie/Downloads/zz/zirp.shp'
districts = '/Users/freddie/Downloads/district/GH_DISTRICTS_260.shp'


def get_coord():

    """get coordinates from user to json """ 
    while True:
        try:
            lon, lat = (input("Enter coordinates separated by a ',':\n").split(","))
            return float(lon), float(lat)
        except ValueError:
            print('check your input')   
    

def coord_json(coords):
    """converts coord tuple to json"""
    coordinates_dictionary = {
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": coords
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


def read_shape_file(file_path):
    """read the a given shapefile to gpd""" 
    file_read = gpd.read_file(file_path)
    file_projected = file_read.to_crs(epsg=3857)
    return file_projected



def get_geoprocess():

    #spatial analysis
    buffer = read_point()['geometry'].buffer(distance = 1200)        
    buffer_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer))
    buffer_df = buffer_df.rename(columns={0:'geometry'}).set_geometry('geometry')
    print(buffer_df)
    buffer_df.to_file(r"/Users/freddie/test2.shp")


    join = gpd.sjoin(read_shape_file(districts), buffer_df, how="inner", op="intersects")
    print('this is a join....\n')
    print(join)
    join.to_file(r"/Users/freddie/test.shp")

    print('preparing another buffer\n')

    return buffer_df

def buffer_point():
    buffer_new = read_point()['geometry'].buffer(distance = 5000)        
    buffer_new_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer_new))
    buffer_new_df = buffer_new_df.rename(columns={0:'geometry'}).set_geometry('geometry')
    print(buffer_new_df)
    return buffer_new_df
    

def get_aoi_towns():
    """get towns that are with the 3000m buffer"""
    towns_in_aoi = gpd.overlay(read_shape_file(towns), buffer_point(), how = 'intersection')
    print("these are the towns we really want to look at")
    print(towns_in_aoi)
    return towns_in_aoi


def add_basemap():
    print("Drawing map, please wait...")
    #plotting to map
    plt.rcParams['figure.figsize'] = [10, 10] #this sets the size of the figure
    fig, myax = plt.subplots()
    read_point().plot(ax=myax, color='red')
    get_geoprocess().plot(ax=myax, ec='gray', alpha=0.2, edgecolor='black')
    get_aoi_towns().plot(ax=myax, color='green')
    src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ctx.add_basemap(ax=myax, source=src_basemap, alpha=0.6, zorder=8)
    plt.show()




def main():
    coord_json(get_coord())                   
    add_basemap() 

if __name__ == '__main__':
    coord_json((2,5))


