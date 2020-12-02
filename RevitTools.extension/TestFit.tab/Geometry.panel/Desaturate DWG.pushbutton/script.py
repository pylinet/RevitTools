'''
Author: Pyline Tangsuvanich
Overrides graphics of all linked CADs to gray. 
'''

# Import modules from RevitPythonWrapper

from rpw import revit, db, ui, UI, DB


# Set active document

doc_active = revit.uidoc.ActiveView

# Collect CAD links
# Note: Because we import DB, we can call on ImportInstance

dwg_collector = db.Collector(of_class = 'ImportInstance', is_type=False)
dwg_elements = dwg_collector.get_elements()

# Collect views

view_collector = db.ViewPlan.collect()


# Set Color

color_gray = DB.Color(80,80,80)

# Create Class for Override

ogs = DB.OverrideGraphicSettings().SetProjectionLineColor(color_gray)

# Start transaction

t = db.Transaction('Set Linked CADs to Gray')
t.Start()

# The SetElementOverrides method requires element ID and override instance

for view in view_collector:
    for dwg in dwg_elements:
        dwg_id = dwg.Id
        dwg.Pinned = False
        view.SetElementOverrides(dwg_id, ogs)
        dwg.Pinned = True

t.Commit()

