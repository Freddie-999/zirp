import csv
import geopandas as gpd

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



def read_shape_file():
    country = gpd.read_file('/Users/freddie/Downloads/district/Districts_Ghana_project.shp')
    country.head()

