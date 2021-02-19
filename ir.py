import csv
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx


filepath = '/Users/freddie/Downloads/data.csv'

foi = input('Enter the name of the facility:\n')
if (foi == ""):
    print('Input cannot be empty')

found = False

with open(filepath) as f:
    csv = csv.DictReader(f)
    for row in csv:
        if (row['Summary'] == foi):
          print(f"Facility's status is {row['Status']} and it's in the {row['Zone']} distrct.")
          found = True
          break


if not found:
    print("No record found.")

country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')


def read_shape_file():
    """read the of country and towns""" #TOdo towns
    country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')
    print(country.shape)
    print(country.head())
    #country.plot()
    plt.show()
read_shape_file()


def add_basemap_():
    """Add a basemap"""
    country_plt = country.plot(edgecolor='black',facecolor='none',
                               linewidth=1,
                               figsize=(9, 9)
                              )
    ctx.add_basemap(country_plt)
    plt.show()
add_basemap_()



def get_coord():
    """get coordinates from user and plot """ 
    pass




def select_dist():
    """select district of interest"""
    pass






