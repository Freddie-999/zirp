import json
from shapely.geometry import mapping, shape

def get_coord():
    """get coordinates from user and plot """ 
    while True:
        try:
            x, y = (input("Enter coordinates separated by a ',':\n").split(","))
            return float(x), float(y)
        except ValueError:
            print('check your input')            

coordinates = get_coord()

print(coordinates)

s = shape(json.loads('{"type": "Point", "coordinates": [0.0, 0.0]}'))
s
<shapely.geometry.point.Point object at 0x...>
print(json.dumps(mapping(s)))
{"type": "Point", "coordinates": [0.0, 0.0]}


def plot_coord():
    """plot coordinates from user on a map"""
    coordplt = Point(coordinates)
    gdf_coordplt = gpd.GeoSeries([coordplt], crs={'init': 'epsg:4326'}).plot()
    plt.show()