# Import modules from RevitPythonWrapper

from rpw import revit, db, ui, UI, DB
from rpw.ui.forms import FlexForm, Label, ComboBox, TextBox, Separator, Button, CheckBox, SelectFromList

# Set active document

doc_active = revit.uidoc.ActiveView
alert = ui.forms.Alert

# Collectors

level_collector = db.Collector(of_class='Level', is_type=False)
level_elements = level_collector.get_elements()

wall_collector = db.Collector(view = doc_active, of_class='Wall', is_type=False)
wall_elements = wall_collector.get_elements()

# Create a dictionary of all Levels

levels_dict = {}

for level in level_elements:
	level_id = level.Id
	keys = level.Name
	values = level_id
	levels_dict[keys] = levels_dict.get(keys, values)

# Create a list of all Levels

levels_list = []
for level in level_elements:
	level_id = levels_list.append(level.Id)


# FlexForm

components = [Label('Test:'),ComboBox('test',levels_dict),Button('Select')]
form = ui.forms.FlexForm('Set Level', components)
form_show = form.show()

# returns a dictionary with one object
form_value = form.values

# returns a list with one object
form_value1 = form_value.values()

# Start transaction

t = db.Transaction()
t.Start()

for wall in wall_elements:
	wall.parameters['Top Constraint'] = form_value1[0]

# because form_value returns a list, you must grab the item object in that list and feed it into the parameter

t.Commit()
