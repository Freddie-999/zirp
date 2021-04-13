import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json

#set paths for shapefiles
towns = '/Users/freddie/Downloads/zz/zirp.shp'
districts = '/Users/freddie/Downloads/district/GH_DISTRICTS_260.shp'
json_coordinates = 'new_coords.geojson'

def get_coord():

    """get coordinates from user to json """ 
    while True:
        try:
            lon, lat = (input("Enter coordinates separated by a ',':\n").split(","))
            return float(lon), float(lat)
        except ValueError:
            print('check your input')   
    

def write_coordinates_to_file(coords, filepath):
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
    with open(filepath, 'w') as f:
        json.dump(coordinates_dictionary, f)



def read_point(filepath):
    """read coordinates on a from the saved .json file"""
    point_df = gpd.read_file('new_coords.geojson')
    point_df_new = point_df.to_crs(epsg=3857)
    return point_df_new


def read_shape_file(file_path):
    """read the a given shapefile to gpd""" 
    file_read = gpd.read_file(file_path)
    file_projected = file_read.to_crs(epsg=3857)
    return file_projected


def get_geoprocess(point_df):

    #spatial analysis
    buffer = point_df['geometry'].buffer(distance = 1200)        
    buffer_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer))
    buffer_df = buffer_df.rename(columns={0:'geometry'}).set_geometry('geometry')
    print(buffer_df)
    buffer_df.to_file(r"/Users/freddie/test2.shp")


    join = gpd.sjoin(read_shape_file(districts), buffer_df, how="inner", op="intersects")
    print('this is a join....\n')
    print(join)
    join.to_file(r"/Users/freddie/test.shp")
    return buffer_df


def buffer_point(point_df):
    buffer_new = point_df['geometry'].buffer(distance = 2500)        
    buffer_new_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer_new))
    buffer_new_df = buffer_new_df.rename(columns={0:'geometry'}).set_geometry('geometry')
    print(buffer_new_df)
    return buffer_new_df
    

def get_aoi_towns(all_towns, buffer_size, how):
    """get towns that are with the 3000m buffer"""
    towns_in_aoi = gpd.overlay(all_towns, buffer_size, how) #(read_shape_file(towns), buffer_point(), how = 'intersection')
    print("these are the towns we really want to look at")
    print(towns_in_aoi)
    return towns_in_aoi


def add_basemap(point_df, buffer_, closest_town):
    print("Drawing map, please wait...")
    #plotting to map
    plt.rcParams['figure.figsize'] = [10, 10] #this sets the size of the figure
    fig, myax = plt.subplots()
    point_df.plot(ax=myax, color='red')
    buffer_.plot(ax=myax, ec='gray', alpha=0.2, edgecolor='black')
    closest_town.plot(ax=myax, color='green')
    src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ctx.add_basemap(ax=myax, source=src_basemap, alpha=0.6, zorder=8)
    plt.show()



def main():
    coordinates_from_user = get_coord()
    write_coordinates_to_file(coordinates_from_user, json_coordinates)
    point_dataframe = read_point(json_coordinates)
    buffered_point = buffer_point(point_dataframe)
    towns_data = get_aoi_towns(read_shape_file(towns), buffered_point, 'intersection')
    add_basemap(point_dataframe,buffered_point ,towns_data) 


if __name__ == '__main__':
    main()


