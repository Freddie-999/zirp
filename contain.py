import shapely.speedups
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
from shapely.geometry import Point
import json
shapely.speedups.enable()


districts = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')
districtboundary_projected = districts.to_crs(epsg=3857)

districts.contains()