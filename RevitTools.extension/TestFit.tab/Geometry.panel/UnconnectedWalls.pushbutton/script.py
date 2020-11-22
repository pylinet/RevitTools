from rpw import db, ui

# COLLECT ALL WALLS

doc = uidoc.Document
# apidocs.co/apps/revit/2020/043960ac-dde4-0f45-249f-8161646a4362.htm

wall_collector = db.Collector(view = doc.ActiveView, of_class='Wall', is_type=False)
wall_elements = wall_collector.get_elements()


# WALLS ON CURRENT LEVEL

for wall in wall_elements:
	param_height = wall.parameters['Unconnected Height']
	param_constraint = wall.parameters['Top Constraint'].AsValueString()
	param_constraint2 = wall.parameters.builtins['WALL_HEIGHT_TYPE']
	print param_height.value
	print param_constraint

selection = ui.Selection(wall_elements)


# START A TRANSACTION
t = Transaction(doc, 'connect unconnected walls')

def set_param(element, ParameterName, Value):
	param_constraint = wall.parameters[ParameterName].Set(Value)

t.Start()

for wall in wall_elements:
	set_param(wall, "Unconnected Height", 12)
    # having trouble changing Top Constraint for some reason.


t.Commit()