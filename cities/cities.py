#!/usr/bin/env python3

import arcpy

arcpy.env.workspace = 'data' # or r'.\data' for windows
 
cities = 'data/ne_10m_populated_places.shp' #cities points
countries = 'data/ne_10m_admin_0_countries.shp' # countries polygon
outpath = 'outputs' #save to this folder
# creating a feature layer for the cities shape file
arcpy.MakeFeatureLayer_management(\
	cities,'cities_layer')
# creating a feature layer for the countries shape file and limit it to US
arcpy.MakeFeatureLayer_management(\
	countries,\
	'countries_layer',\
	""" "NAME" = 'United States' """)
# in_feature, out_feature, where_clause
# you can get the where clause by checking the attr table in the shape file

#select cities_layer  that lay within countries_layer, saved in the cities_layer
arcpy.SelectLayerByLocation_management('cities_layer', 'WITHIN', 'countries_layer')
# layer_to_be_selected, type_of_overlap, boundry_layer


#save the slected points to a new feature layer
arcpy.FeatureClassToFeatureClass_conversion('cities_layer', outputs, 'cities_us')
#layer_from, save_folder, layer_to



