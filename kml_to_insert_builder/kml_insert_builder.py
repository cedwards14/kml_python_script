
from fastkml import kml
from bs4 import BeautifulSoup


k = kml.KML()
kml_file = "BlueTrail.kml"
with open(kml_file, 'rt')as myfile:
    doc = myfile.read().encode('utf-8')

k.from_string(doc)
features = list(k.features())
soup = BeautifulSoup(doc, "xml")

id_lat_long = []
my_latlongs = []
my_lat = []
my_long = []


for coord in soup.find_all('Placemark'):
    for coords in coord.find_all('coordinates'):
        my_latlongs = coords.text.replace(',0', '').split(",")
    my_lat.append(my_latlongs[1].split())
    my_long.append(my_latlongs[0].split())

i = 11
while i < len(my_lat):
    value = [i+1] + my_lat[i] + my_long[i]
    id_lat_long.append(value)
    i += 1


my_insert = []
file = open("latLong.txt", "w")
for item in id_lat_long:
    value = """insert into Polylines(polylineId, cityId, markerId, trailId, lat, long) values({0}, 1, 40, 2, {1}, {2});""".format(item[0], item[1], item[2])
    file.write(value)    

print(my_insert)
