import geopandas as gpd
import pandas as pd

def import_shp(path='./dados/Shapefiles/pddua/QTR_1.shp'):
    shapefile = gpd.read_file("./dados/Shapefiles/pddua/QTR_1.shp")
    shapefile['MZUEUQRT'] = (shapefile['MZ']*1000000) + (shapefile['UEU']*1000) + (shapefile['QTR'])
    shapefile.set_index(keys='MZUEUQRT', inplace=True)

    return shapefile