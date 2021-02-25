from rpw import db

# is_type=False allows it to only return FamilyInstance rather than also FamilySymbol

# LEVEL COLLECTOR
level_filter = lambda x:x.Name == 'LEVEL 1'
levels = db.Collector(of_class='Level', is_type=False,where=level_filter)
level_elements = levels.get_elements()
print 'levels', level_elements

# ROOM COLLECTOR
# create a filter that will pass through the 'where' method
room_filter = lambda x:x.name == 'STUDIO'
room_collector = db.Collector(of_category='OST_Rooms', is_type=False, where=room_filter)
room_elements = room_collector.get_elements()
print 'room elements', room_elements

# room location

for room in room_elements:
	room_name = room.Location
print room_name.Point





# FURNITURE COLLECTOR
# OST_Furniture will collect all of the Instances and not the Parent Family.
# create a furniture type name filter
# furn_filter = lambda x:x.name == '54"'
#is_type=False allows it to only return FamilyInstance rather than also FamilySymbol
furn_collector = db.Collector(of_category='OST_Furniture', is_type=False)
furn_elements = furn_collector.get_elements()
print 'furn elements', furn_elements

# create a dictionary / histogram
counts = {}
for furn in furn_collector: # for loop to iterate through each item in the dictionary
	furn_name = furn.Name   # gets the name of the Symbol
	counts[furn_name] = counts.get(furn_name,0)+1         # counts how many times the object occurs in the dictionary
print 'keys, values', counts

print("\n")
print 'keys', counts.keys() # returns keys
print 'counts', counts.values()   # returns values
print("\n")

# prints the total amount of items in the Collection
# prints the parent Family Name
print furn_collector.GetElementCount(),  furn.Symbol.FamilyName
print("\n")

# create a new dictionary that returns values that satisfy the filter
studio = {}
for (key, value) in counts.items():
	if ('54"' in str(key)):
		studio[key] = value
	# originally tried if (key = '54"') but that did not work. need to convert key to a string.
print studio




# trying to get the room name the elements are in
phase = list(doc.Phases)[-1]
for f in furn_elements:
	room_name = f.Room[phase]
print 'room name', room_name
print("\n")


