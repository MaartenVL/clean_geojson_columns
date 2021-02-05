import geopandas as gpd

def read_json(filename):
    """

    :param filename:
    :return:
    """
    gdf = gpd.read_file(filename)
    return gdf

def remove_columns(gdf, list_columns):
    """

    :param list_columns:
    :return:
    """

    for col in list_columns:
        #remove the col
        del gdf[col]
        print( "removed " + col)

    return gdf

def geopandas_to_geojson(file2convert,output_name):
    """

    :return:
    """

    file2convert.to_file(output_name, driver='GeoJSON')

