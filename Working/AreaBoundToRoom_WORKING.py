# import modules from RPW & Revit API
from rpw import db, ui, UI, DB
# from Autodesk.Revit import UI, DB, Creation
# import the CurveArray method
# from Autodesk.Revit.DB import CurveArray


#print dir(revit.doc.Create)
#print dir(DB)

# set the plug in to run on the active document
doc = __revit__.ActiveUIDocument.Document
# app = doc.Application
docCreate = doc.Create
# NOT creation. it is Create property under Document
# appCreation = app.Create

# collect areas
area_collector = db.Collector(view=doc.ActiveView, of_category = 'OST_AreaSchemeLines', is_type = False)
# collect area elements
area_elements = area_collector.get_elements()

# QC to make sure its being collected
# print area_collector
# print area_elements

# area lines are MODEL LINE ELEMENTS. so they belong to the MODEL LINE CLASS.

# need to use DB dot notation to access the method in a different module
curve_array = DB.CurveArray()
# wouldn't work if its a lower case db or if db doesn't exist
# couldn't just do curve_array = [] as an empty list because the NewBoundaryLines method needs a CurveArray as an input
# once I knew this, 

# will only work if you are in the area boundary view. it will not work if there are no curves in the view.
# sketchplane is a property of the model line class and is required to make NewBoundaryLines
for curve in area_elements:
	sketchplane = curve.SketchPlane
	curves = curve_array.Append(curve.GeometryCurve)
	print curve_array

# QC to make sure it worked
# print curve_array
# print sketchplane


t = db.Transaction('room bounds')

t.Start()

# thought process: goal was to convert existing area bound to room separation lines so you don't need to "pick lines" or go through
# the tedious process of redrawing
# once i knew this, i searched the API to see which method would allow me to create these new lines
# in order to figure out what i needed from the area elements, need to look up the method to see what the inputs are
docCreate.NewRoomBoundaryLines(sketchplane, curve_array, view=doc.ActiveView)

#wait -- why does this work under docCreate, which is doc.Create? the new room bound is located under Creation not create...
# Autodesk.Revit.Creation Namespace

t.Commit()