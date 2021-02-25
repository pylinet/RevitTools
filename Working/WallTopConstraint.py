# Import modules from RevitPythonWrapper

from rpw import revit, db, ui, UI, DB
create = revit.doc.Create

# Set active document

doc_active = revit.uidoc.ActiveView
alert = ui.forms.Alert

wall_collector = db.Collector(view = doc_active, of_class='Wall', is_type=False)
wall_elements = wall_collector.get_elements()


level_collector = db.Collector(view = doc_active, of_class='Level', is_type=False)
level_elements = level_collector.get_elements()
#print level_elements

# WALLS ON CURRENT LEVEL

for wall in wall_elements:
	param_height = wall.parameters['Unconnected Height']
	param_constraint = wall.parameters['Top Constraint']
	param_constraint2 = wall.parameters.builtins['WALL_HEIGHT_TYPE']
	elementid = param_constraint.AsElementId()
	#element1 = db.Element.from_int(elementid)
#	print param_height.value
#	print param_constraint
#	print param_constraint.AsValueString()
#	print elementid

	
#element1 = db.Element.from_id(element1)
#element2 = db.Element.from_int(Integer)

# couldn't get element just from element ID..but there must be a way?!

#need to do a level collector

#elements = []
#elements.append(doc_active.GetElement(-1))



#selection = ui.Selection(wall_elements)


# START A TRANSACTION
t = db.Transaction('connect unconnected walls')

def set_param(element, ParameterName, Value):
	param_constraint = wall.parameters[ParameterName].Set(elementid)
#Set(elementid.InvalidElementId) will set it to -1, which is unconnected

t.Start()

for wall in wall_elements:
	set_param(wall, "Top Constraint", -1)
    # having trouble changing Top Constraint for some reason.

for wall in wall_elements:
	param_constraint = wall.parameters['Top Constraint']
	#print param_constraint

t.Commit()


