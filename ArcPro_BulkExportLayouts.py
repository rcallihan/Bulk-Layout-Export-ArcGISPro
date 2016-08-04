import arcpy

#insert your own path here
export_path = 'C:\\Users\\rcallihan\\Documents\\gen\\'

p = arcpy.mp.ArcGISProject("CURRENT")
list_layouts = p.listLayouts()

for f in list_layouts:
	layout_name = f.name
	full_export_path = export_path + layout_name
	f.exportToPDF(full_export_path)