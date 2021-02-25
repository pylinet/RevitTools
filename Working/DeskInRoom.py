from rpw import db


# ROOM COLLECTOR
# create a filter that will pass through the 'where' method
room_filter = lambda x:x.name == 'STUDIO'
room_collector = db.Collector(of_category='OST_Rooms', is_type=False, where=room_filter)
room_elements = room_collector.get_elements()


# room location

for room in room_elements:
	room_name = room.Location
	#print room_name

furniture_filter = lambda x:x.name == '48"'
furn_collector = db.Collector(of_category='OST_Furniture', is_type=False,where=furniture_filter)
furn_elements = furn_collector.get_elements()


counts = {}
for furn in furn_collector: # for loop to iterate through each item in the dictionary
	furn_name = furn.Name   # gets the name of the Symbol
	furn_parameter=furn.GetParameters('Name')
	counts[furn_name] = counts.get(furn_name,0)+1         # counts how many times the object occurs in the dictionary
	#print furn_parameter

print list(furn.GetParameters('Name'))

#print counts

for f in furn_elements:
	location = f.Location
	location_point = location.Point
	#print location.Point


