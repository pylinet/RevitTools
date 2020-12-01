'''
Author: Pyline Tangsuvanich
Set top constraint level of all walls in current view.
'''

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

# FlexForm

components = [Label('Select Level:'),ComboBox('Level',levels_dict),Button('Select')]
form = ui.forms.FlexForm('Set Level', components)
form_show = form.show()

# Returns a dictionary with one object
form_value_dict = form.values

# Returns a list with just the value in the dictionary (no key). You need the value because that is the element ID object.
form_value_list = form_value_dict.values()

# Start transaction

t = db.Transaction()
t.Start()

# Set the Top Constraint parameter to the level that was selected via FlexForm

for wall in wall_elements:
	wall.parameters['Top Constraint'] = form_value_list[0]

# Because form_value_list returns a list, you must grab the item object in that list via [] and feed it into the parameter. If you dont, you get the following error:
# Exception : System.Exception: Wrong Storage Type: [<type 'ElementId'>]:[<type 'list'>:[<Autodesk.Revit.DB.ElementId object at 0x0000000000001F22 [665247]>]]

t.Commit()
