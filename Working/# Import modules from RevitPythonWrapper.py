# Import modules from RevitPythonWrapper

from rpw import revit, db, ui, UI, DB
create = revit.doc.Create

# Set active document

doc_active = revit.uidoc.ActiveView
alert = ui.forms.Alert

#this only works if view is removed..
phase_collector = db.Collector(of_category='OST_Phases', is_type=False)
phase_elements = phase_collector.get_elements()


level_collector = db.Collector(of_class='Level', is_type=False)
level_elements = level_collector.get_elements()
print level_elements

wall_collector = db.Collector(view = doc_active, of_class='Wall', is_type=False)
wall_elements = wall_collector.get_elements()


levels = []
for level in level_elements:
	level_id = levels.append(level.Id)

print levels[1]

phases = []
for phase in phase_elements:
	phase_id = phases.append(phase.Id)

print phases[1]

t = db.Transaction()
t.Start()

for wall in wall_elements:
	#param_height = wall.parameters['Unconnected Height']
	#param_constraint = wall.parameters['Top Constraint'] = levels[1]
	param_constraint3 = wall.parameters['Phase Created']
	#alternate method below
	#if param_constraint3:
	#	param_constraint3.Set(phases[1])
	

#another method below
def set_param(element, ParameterName, Value):
	param_constraint3 = wall.parameters[ParameterName].Set(Value)

for wall in wall_elements:
	set_param(wall, "Phase Created", phases[1])

t.Commit()



