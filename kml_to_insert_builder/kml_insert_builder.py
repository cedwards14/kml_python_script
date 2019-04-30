
from bs4 import BeautifulSoup

id_lat_long = []
my_latlongs = []
my_lat = []
my_long = []
my_markers = []

# marker_id = 1
# trail_id = 1
# kml_file = "GreenTrail.kml"

marker_id = 337
trail_id = 2
kml_file = "BlueTrail.kml"


# marker_id = 533
# trail_id = 3
# kml_file = "RedTrail.kml"


# marker_id = 669
# trail_id = 4
# kml_file = "OrangeTrail.kml"



with open(kml_file, 'rt')as myfile:
    doc = myfile.read().encode('utf-8')


soup = BeautifulSoup(doc, "xml")


for coord in soup.find_all('Placemark'):
    for markers in coord.find_all('description'):
        my_markers.append(markers.text)
    for coords in coord.find_all('coordinates'):
        # coordinates comes with a ,0 at the end so I want to remove it
        my_latlongs = coords.text.replace(',0', '').split(",")
        # removes the empty space
    my_lat.append(my_latlongs[1].split())
    my_long.append(my_latlongs[0].split())


print(len(my_lat))
print(len(my_markers))
i = 0
# put my id, lat and long into a new list
while i < len(my_lat):
    value = [marker_id] + my_lat[i] + my_long[i]
    id_lat_long.append(value)
    id_lat_long[i].append(my_markers[i])
    id_lat_long[i].append(trail_id)
    i += 1
    marker_id += 1


file = open("latLong.txt", "w")
for item in id_lat_long:
    value = """\n insert into Polylines(polylineId, cityId, markerId, trailId, lat, long) values({0}, 1, {3}, {4}, {1}, {2});""".format(
        item[0], item[1], item[2], item[3], item[4])
    file.write(value)


# print(len(id_lat_long))

markerId = 1
trailId = 1
index = 0
kml_list = ["GreenTrail.kml", "BlueTrail.kml", "RedTrail.kml", "OrangeTrail.kml" ]

for trail in kml_list:
    with open(trail[index], 'rt')as myfile:
        doc = myfile.read().encode('utf-8')
    soup = BeautifulSoup(doc, "xml")
    
    for coord in soup.find_all('Placemark'):
        for markers in coord.find_all('description'):
            my_markers.append(markers.text)
        for coords in coord.find_all('coordinates'):
            # coordinates comes with a ,0 at the end so I want to remove it
            my_latlongs = coords.text.replace(',0', '').split(",")
            # removes the empty space
        my_lat.append(my_latlongs[1].split())
        my_long.append(my_latlongs[0].split())
