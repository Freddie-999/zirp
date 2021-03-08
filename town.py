import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json

towns = gpd.read_file('/Users/freddie/Downloads/ghana_location/ghana_location.shp')
towns.plot()
plt.show()