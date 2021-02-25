# Get Wall Types Method 1

from rpw import db

wall_types_collector = db.WallType.collect()
wall_types_collector.get_elements()

for wall_type in wall_types_collector:
	print wall_type.FamilyName


# Get Wall Types Method 2

from rpw import db

walls = db.Collector(of_category='OST_Walls')
walls = walls.get_elements()

for w in walls:
	walls = w.get_family()
	wall_name = walls.name

print wall_name

