import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json


def main():
    def get_coord():
        """get coordinates from user to json """ 
        while True:
            try:
                lon, lat = (input("Enter coordinates separated by a ',':\n").split(","))
                return float(lon), float(lat)
            except ValueError:
                print('check your input')   
        
    def coord_json():
        """converts coord tuple to json"""
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


    def read_shape_file():
        """read the districts to gpd""" 
        districts = gpd.read_file('/Users/freddie/Downloads/district/GH_DISTRICTS_260.shp')
        districtboundary_projected = districts.to_crs(epsg=3857)
        return districtboundary_projected


    def read_towns():
        """get coordinates of towns"""
        df = pd.read_csv('/Users/freddie/Downloads/jira_data.csv')
        points = df.apply(lambda row: Point(row.Lon, row.Lat), axis=1)
        towns_gdf = gpd.GeoDataFrame(df, geometry=points)
        proj = towns_gdf.set_crs(epsg=3857)
        proj.set_index('Summary', inplace=True)
        proj.to_csv("/Users/freddie/Downloads/new.csv", index=True, mode='w')
        return proj


    def get_nearest_town():
        """find the nearest town to incident"""
        pass


    def get_info():
        """return the info for the nearest town"""
        pass




    def get_geoprocess():


        #spatial analysis
        buffer = mypoint['geometry'].buffer(distance = 1200)
        buffer_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer))
        buffer_df = buffer_df.rename(columns={0:'geometry'}).set_geometry('geometry')
        print("this is buffer 1.....\n")
        print(buffer_df)
        return buffer_df
        buffer_df.to_file(r"/Users/freddie/test2.shp")

        join = gpd.sjoin(mydistrict, buffer_df, how="inner", op="intersects")
        print('this is a join....\n')
        print(join)
        join.to_file(r"/Users/freddie/test.shp")

        print('preparing another buffer\n')

        buffer2 = mypoint['geometry'].buffer(distance = 50000)
        buffer2_df = gpd.GeoDataFrame(gpd.GeoSeries(buffer))
        buffer2_df = buffer2_df.rename(columns={0:'geometry'}).set_geometry('geometry')
        print("this is buffer 2.......\n")
        print(buffer2_df)
        buffer2.to_file(r"/Users/freddie/luck.shp")

        shw = mytowns['geometry'].within(buffer2_df)
        shw.to_csv("tryme.csv", index=True, mode="w")
        print(shw)

    def add_basemap():
        print("Drawing map, please wait...")
        #plotting to map
        plt.rcParams['figure.figsize'] = [10, 10] #this sets the size of the figure
        fig, myax = plt.subplots()
        #mydistrict.plot(ax=myax, ec='gray', alpha=0.2, column='Name')
        get_geoprocess().plot(ax=myax, ec='gray', alpha=0.2, edgecolor='black')
        mypoint.plot(ax=myax, color='red')
        #join.plot(ax=myax, ec='gray', alpha=0.2, edgecolor='black')
        #mytowns.plot(ax=myax, color='green')
        print("trying to add points")
        #read_towns().plot(ax=myax)
        
        src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        ctx.add_basemap(ax=myax, source=src_basemap, alpha=0.6, zorder=8)
        plt.show()


    coordinates = get_coord()
    coord_json()                   
    mypoint = read_point()
    mydistrict = read_shape_file()
    mytowns = read_towns()
    get_geoprocess()
    add_basemap() 

if __name__ == '__main__':
    main()


