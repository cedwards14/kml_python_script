
from fastkml import kml
from bs4 import BeautifulSoup

id_lat_long = []
my_latlongs = []
my_lat = []
my_long = []


kml_file = "BlueTrail.kml"

with open(kml_file, 'rt')as myfile:
    doc = myfile.read().encode('utf-8')


soup = BeautifulSoup(doc, "xml")




for coord in soup.find_all('Placemark'):
    for coords in coord.find_all('coordinates'):
        # coordinates coems with a ,0 at the end so i want to remove it
        my_latlongs = coords.text.replace(',0', '').split(",")
        # removes the empty space
    my_lat.append(my_latlongs[1].split())
    my_long.append(my_latlongs[0].split())


# put my id, lat and long into a new list
i = 11
while i < len(my_lat):
    value = [i+1] + my_lat[i] + my_long[i]
    id_lat_long.append(value)
    i += 1



file = open("latLong.txt", "w")
for item in id_lat_long:
    value = """\n insert into Polylines(polylineId, cityId, markerId, trailId, lat, long) values({0}, 1, 40, 2, {1}, {2});""".format(item[0], item[1], item[2])
    file.write(value)    

print(file)
