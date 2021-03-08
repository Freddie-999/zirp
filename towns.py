from shapely.geometry import Point
from geopandas import GeoDataFrame
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt



def plotPoint():
    df = pd.read_csv('/Users/freddie/Downloads/jira_data.csv')
    geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
plotP oint()