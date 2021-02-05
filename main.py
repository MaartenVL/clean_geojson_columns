from geo_functions import *

file = "Hydranten.geojson"
list_columns = ["G3E_FID",
               "NOMINALE_D",
               "X",
               "Y",
               "CREATE_DAT"]


gpd_file = read_json(filename=file)
gpd_cleaned = remove_columns(gdf=gpd_file,
                             list_columns=list_columns)
geojson =  geopandas_to_geojson(file2convert=gpd_cleaned,
                                output_name="hydranten_cleaned.geojson")
print("q")