
from bs4 import BeautifulSoup

id_lat_long = []
my_latlongs = []
my_lat = []
my_long = []
my_markers = []
complete_list = []
markerId = 1
trailId = 1
i = 0

kml_list = ["GreenTrail.kml", "BlueTrail.kml", "RedTrail.kml", "OrangeTrail.kml" ]

for trail in kml_list:
    with open(trail, 'rt')as myfile:
        doc = myfile.read().encode('utf-8')
    soup = BeautifulSoup(doc, "xml")
    
    for coord in soup.find_all('Placemark'):
        for coords in coord.find_all('coordinates'):
            # coordinates comes with a ,0 at the end so I want to remove it
            my_latlongs = coords.text.replace(',0', '').split(",")
            # removes the empty space
        my_lat.append(my_latlongs[1].split())
        my_long.append(my_latlongs[0].split())

        # put my id, lat and long into a new list
    while i < len(my_lat):
        value = [markerId] + my_lat[i] + my_long[i]
        id_lat_long.append(value)
        id_lat_long[i].append(trailId)
        i += 1
        markerId += 1    
    trailId+=1

file = open("latLong.txt", "w")
for item in id_lat_long:
    value = """\n insert into Polylines(polylineId, cityId, trailId, lat, long) values({0}, 1, {3}, {1}, {2});""".format(item[0], item[1], item[2], item[3])
    file.write(value)
    
         