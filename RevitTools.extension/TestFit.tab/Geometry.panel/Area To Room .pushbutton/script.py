'''
Author: Pyline Tangsuvanich
Convert existing area boundary lines into room separator lines.
'''

# Import modules from RevitPythonWrapper

from rpw import revit, db, ui, UI, DB
create = revit.doc.Create

# Set active document

doc_active = revit.uidoc.ActiveView

# Collect area boundary lines in the current view

area_collector = db.Collector(view=doc_active, of_category = 'OST_AreaSchemeLines', is_type = False)
area_elements = area_collector.get_elements()

# Create an empty array for area boundary curves
# Area boundaries are model lines and need to be converted to curves

curve_array = DB.CurveArray()

for curve in area_elements:
		sketchplane = curve.SketchPlane
		curves = curve_array.Append(curve.GeometryCurve)

# If there are no area boundary lines in the view, return an error
# Else, start the transaction that will convert them into room boundary lines

if len(area_elements) == 0:
	alert('No Area Boundaries in View', title="Error")
else:
	t = db.Transaction('room bounds')
	t.Start()
	create.NewRoomBoundaryLines(sketchplane, curve_array, doc_active)
	t.Commit()