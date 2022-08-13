#!/usr/bin/env python3

#search Cursor: loop over NAME column in "countries" shape file and print them

import arcpy

arcpy.env.workspace = 'data'

points = 'data/ne_10m_populated_places.shp'
countires = 'data/ne_50m_admin_0_countries.shp'
outpath = 'outputs'

arcpy.MakeFeatureLayer_management(points, 'cities_layer')
with arcpy.da.SearchCursor(countries, ['FID','NAME']) as countries:
	for country in countries:
		arcpy.MakeFeatureLayer_management(countires, 'country_layer', """ 'FID' = '{}' """.format(country[0]))
		arcpy.SelectLayerByLocation_management('cities_layer', 'WITHIN', 'country_layer')
		arcpy.FeatureClassToFeatureClass_conversion(points_layer, outpath, 'cities_in_{}'.format(coountry[1]))
