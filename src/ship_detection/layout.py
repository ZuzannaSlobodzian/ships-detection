import ee
import geemap.foliumap as geemap
from .regions import combine_regions


def sentinel1(date, region):
    collection = (
        ee.ImageCollection('COPERNICUS/S1_GRD')
        .filterBounds(region)
        .filterDate(date[0], date[1])
    )

    images = collection.limit(10)  
    clipped_images = images.map(lambda img: img.clip(region))
    mosaic_image = clipped_images.mosaic()
    vis_params = {'min': -25, 'max': 0}
    return [mosaic_image, vis_params]

def prepare_map(date, region):
    map = geemap.Map(center=(30, 0), zoom=3)

    mosaic_image_sent1, vis_params_sent1 = sentinel1(date, region)
    map.addLayer(mosaic_image_sent1, vis_params_sent1, 'Sentinel-1')
    return map

def prepare_basemap():
    basemap = geemap.Map(center=(30, 0), zoom=3)
    combined_geom = combine_regions()
    layer = ee.FeatureCollection(ee.Feature(combined_geom)).style(**{
        'color': '0000FF',  
        'width': 1,
        'lineType': 'solid',
        'fillColor': 'abc8ff61'
    })

    basemap.addLayer(layer, {}, "Regions")
    return basemap

