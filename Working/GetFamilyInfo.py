from rpw import db, ui

# FURNITURE COLLECTOR
furn_collector = db.Collector(of_category='OST_Furniture', is_type=False)
furn_elements = furn_collector.get_elements()
print furn_elements

print ("\n")

Units = []
NoUnits = []
MissingUnits = []


print ("\n")

for furn in furn_elements:
	furn_symb = furn.get_symbol()
	furn_getfam = furn.get_family()
	furn_name = furn_getfam.name
	if ('GRP' in furn_name):
		MissingUnits.append(furn_getfam)

for furn in furn_elements:
	furn_symb = furn.get_symbol()
	furn_getfam = furn.get_family()
	param = int(furn_symb.parameters['Hana-SeatingCapacity'].value)
	if (param > 0):
		Units.append(furn)
	else:
		NoUnits.append(furn)
		#rather than put furn in there, put furn_getfam
		#select only works with FamilyInstance..doesn't work with Symbols or Family not sure why


print ("\n")

print 'THESE FAMILIES HAVE HANA-SEATING CAPACITY', Units, ("\n")
print 'THESE FAMILIES DO NOT', NoUnits, ("\n")
print 'THESE FAMILIES HAVE GRP IN NAME', MissingUnits

selection = ui.Selection(Units)