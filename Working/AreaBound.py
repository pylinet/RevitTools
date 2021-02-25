
from rpw import db, ui

app = uidoc.Application
doc = uidoc.Document

area_collector = db.Collector(view=doc.ActiveView, of_category = 'OST_AreaSchemeLines', is_type = False)
area_elements = area_collector.get_elements()

print area_collector

#curve_array = app.Create.NewCurveArray
curve_array = []

for curve in area_elements:
	curves = curve_array.append(curve.GeometryCurve)
	# sketchplane = curve.SketchPlane

print curve_array
print sketchplane


# START A TRANSACTION
t = Transaction(doc, 'room bounds')


#t.Start()
doc.Create.NewRoomBoundaryLines(sketchplane, curve_array, view=doc.ActiveView)


#t.Commit()
















from rpw import db, ui
from Autodesk.Revit.Creation import Application

doc = uidoc.Document
app = doc.Application
docCreation = doc.Create
appCreation = app.Create


area_collector = db.Collector(view=doc.ActiveView, of_category = 'OST_AreaSchemeLines', is_type = False)

area_elements = area_collector.get_elements()

print area_collector
print area_elements

selection = ui.Selection(area_elements)

curve_array = CurveArray()


for curve in area_elements:
	sketchplane = curve.SketchPlane
	curves = curve_array.Append(curve.GeometryCurve)
	print curve_array

print curve_array
print sketchplane


# START A TRANSACTION
t = Transaction(doc, 'room bounds')


t.Start()
docCreation.NewRoomBoundaryLines(sketchplane, curve_array, view=doc.ActiveView)
#getting an error - expected CURVE ARRAY and got LIST


t.Commit()