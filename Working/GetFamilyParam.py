from rpw import db

# FURNITURE COLLECTOR
# OST_Furniture will collect all of the Instances and not the Parent Family.
# create a furniture type name filter
# furn_filter = lambda x:x.name == '54"'

# how to unwrap/unwrite a lambda?
# for x in furn_collector:
#	furn_filter2 = x.Name == '54"'

# is_type=False allows it to only return FamilyInstance rather than also FamilySymbol

furn_collector = db.Collector(of_category='OST_Furniture', is_type=False)
furn_elements = furn_collector.get_elements()


for furn in furn_elements:
	furn_symb = furn.get_symbol()
	furn_getfam = furn.get_family()
	param = furn_symb.parameters['Hana-SeatingCapacity'].value
	print furn_getfam.name
	print param



