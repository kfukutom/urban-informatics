import geopandas
from geodatasets import get_path

path_to_data = get_path("nybb")
gdf = geopandas.read_file(path_to_data, driver="GeoJSON")
gdf = gdf.set_index("BoroName")
gdf["Area"] = gdf.area

# Retrieve Boundary
gdf['boundary'] = gdf.boundary
gdf['boundary']
"""
Since we have saved boundary as a new column, we now have two 
geometry columns in the same GeoDataFrame. We can also create
new geometries, which could be, for example, a buffered version
of the origional one (i.e., GeoDataFrame.buffer(10))
"""
gdf['centroid'] = gdf.centroid
# measuring distances
first_point = gdf['centroid'].iloc[0]
gdf['distance'] = gdf['centroid'].distance(first_point)
gdf["distance"].mean()
gdf.plot("area", legend=True)
gdf.explore("area", legend=False)


