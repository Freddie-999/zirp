import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx



country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')


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

def add_basemap_():
    """Add a basemap"""
    country_plt = country_new.plot(figsize=(9, 16), zorder=10, ec='gray', alpha=0.25)
    #src_basemap = ctx.providers.Stamen.Terrain
    src_basemap = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
    ctx.add_basemap(country_plt, source=src_basemap, alpha=0.6, zorder=8)
    plt.show()
    
add_basemap_()



def get_coord():
    """get coordinates from user and plot """ 
    pass




def select_dist():
    """select district of interest"""
    pass






