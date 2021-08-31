import ee
from ee_plugin import Map

Landsat8 = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')

Map.setCenter(13, 11, 5)
fc = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017").filter(ee.Filter.eq('country_co', 'NI'))


# 2015 Landsat 7 max-pixel composite
collection15 = ee.ImageCollection('LE7_L1T').filterDate("2015-05-01", "2015-8-31") \
      .filterBounds(fc)
image1_15 = collection15.max()

# 2016 Landsat 7 median-pixel composite
collection16 = ee.ImageCollection('LE7_L1T').filterDate("2016-05-01", "2016-8-31") \
      .filterBounds(fc)
image1_16 = collection16.max()

# 2010 Landsat 7 median-pixel composite
collection10 = ee.ImageCollection('LE7_L1T').filterDate("2010-05-01", "2010-8-31") \
      .filterBounds(fc)
image1_10 = collection10.max()

# 2007 Landsat 7 median-pixel composite
collection7 = ee.ImageCollection('LE7_L1T').filterDate("2007-05-01", "2007-8-31") \
      .filterBounds(fc)
image1_7 = collection7.max()

# 2020 Landsat 8 median-pixel composite
collection20 = ee.ImageCollection(Landsat8).filterDate("2020-05-01", "2020-8-31") \
      .filterBounds(fc)
image1_20 = collection20.max()

# 2007 Landsat 8 median-pixel composite
L8collection7 = ee.ImageCollection(Landsat8).filterDate("2013-05-01", "2013-8-31") \
      .filterBounds(fc)
L8image1_07 = L8collection7.max()

#CLIP TO CLEAN ROI OF ADM 0
image2_15 = image1_15.clipToCollection(fc)

image2_16 = image1_16.clipToCollection(fc)

image2_10 = image1_10.clipToCollection(fc)

image2_7 = image1_7.clipToCollection(fc)

image2_20 = image1_20.clipToCollection(fc)

L8image2_07 = L8image1_07.clipToCollection(fc)


#NDWI- annual
image2_15_ndwi=image2_15.normalizedDifference(['B5','B4']);
Map.addLayer(image2_15_ndwi,{'min':-1, 'max':1, 'palette':['red', 'white', 'blue']}, 'NDWI 2015', True)

image2_16_ndwi=image2_16.normalizedDifference(['B5','B4']);
Map.addLayer(image2_16_ndwi,{'min':-1, 'max':1, 'palette':['red', 'white', 'blue']}, 'NDWI 2016', True)

image2_10_ndwi=image2_10.normalizedDifference(['B5','B4']);
Map.addLayer(image2_10_ndwi,{'min':-1, 'max':1, 'palette':['red', 'white', 'blue']}, 'NDWI 2010', True)

image2_7_ndwi=image2_7.normalizedDifference(['B5','B4']);
Map.addLayer(image2_7_ndwi,{'min':-1, 'max':1, 'palette':['red', 'white', 'blue']}, 'NDWI 2007', True)

image2_20_ndwi=image2_20.normalizedDifference(['B6','B5']);
#Map.addLayer(image2_20_ndwi,{'min':-1, 'max':1, 'palette':['red', 'white', 'blue']}, 'NDWI 2020',True)

#NDWI Difference
ndwiDifference_07_16 = image2_16_ndwi.subtract(image2_7_ndwi)

ndwiParams = {'min': -0.5, 'max': 0.5, 'palette': ['FF0000', 'FFFFFF', '0000FF']}

Map.addLayer(ndwiDifference_07_16, ndwiParams, 'NDwI difference 2007 - 2016')

ndwiDifference_07_20 = image2_20_ndwi.subtract(image2_7_ndwi)
Map.addLayer(ndwiDifference_07_20, ndwiParams, 'NDwI difference 2007 - 2020')


#NDVI- annual
image2_15_ndvi=image2_15.normalizedDifference(['B4','B3']);
Map.addLayer(image2_15_ndvi,{'min':-1, 'max':1, 'palette':['red', 'yellow', 'green']}, 'NDVI 2015', True)

image2_16_ndvi=image2_16.normalizedDifference(['B4','B3']);
Map.addLayer(image2_16_ndvi,{'min':-1, 'max':1, 'palette':['red', 'yellow', 'green']}, 'NDVI 2016', True)

image2_10_ndvi=image2_10.normalizedDifference(['B4','B3']);
Map.addLayer(image2_10_ndvi,{'min':-1, 'max':1, 'palette':['red', 'yellow', 'green']}, 'NDVI 2010', True)

image2_7_ndvi=image2_7.normalizedDifference(['B4','B3']);
Map.addLayer(image2_7_ndvi,{'min':-1, 'max':1, 'palette':['red', 'yellow', 'green']}, 'NDVI 2007', True)

image2_20_ndvi=image2_20.normalizedDifference(['B5','B4']);
Map.addLayer(image2_20_ndvi,{'min':-1, 'max':1, 'palette':['red', 'yellow', 'green']}, 'NDVI 2020', True)

L8image2_07_ndvi=L8image2_07.normalizedDifference(['B5','B4']);
Map.addLayer(L8image2_07_ndvi,{'min':-1, 'max':1, 'palette':['red', 'yellow', 'green']}, 'NDVI 2013 L8', True)

#NDVI Difference
ndviDifference_07_16 = image2_16_ndvi.subtract(image2_7_ndvi)

Map.addLayer(ndviDifference_07_16, {'palette':['red', 'yellow', 'green']}, 'NDVI difference 2007 - 2016')
ndviDifference_07_20 = image2_20_ndvi.subtract(image2_7_ndvi)

Map.addLayer(ndviDifference_07_20, {'palette':['red', 'yellow', 'green']}, 'NDVI difference 2007 - 2020')
L8ndviDifference_07_20 = image2_20_ndvi.subtract(L8image2_07_ndvi)

Map.addLayer(L8ndviDifference_07_20, {'palette':['red', 'yellow', 'green']}, 'NDVI difference 2013 - 2020 L8')