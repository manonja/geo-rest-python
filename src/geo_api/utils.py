import random
from datetime import datetime
from functools import partial

import pyproj
from shapely.geometry import Polygon
from shapely.ops import transform

from geo_api.models import CountryLightPollutionArea, GeoFeature


def generate_random_point_feature():
    random_lat = round(random.uniform(-90, 90), 6)
    random_lon = round(random.uniform(-180, 180), 6)

    return GeoFeature(
        type="Feature",
        geometry={"type": "Point", "coordinates": [random_lon, random_lat]},
        properties={"name": f"Random Point {random.randint(1000, 9999)}"},
    )


# Creates polygon geometries suitable for country-level light pollution areas.
# It generates random coordinates within specified bounds and creates circular polygons around these points.


def generate_random_polygon_feature(
    country_name, min_lat, max_lat, min_lon, max_lon, num_vertices=5
):
    # Initialize projections
    wgs84 = pyproj.Proj("epsg:4326")
    web_mercator = pyproj.Proj("epsg:3857")

    project_to_web_mercator = partial(pyproj.transform, wgs84, web_mercator)
    project_to_wgs84 = partial(pyproj.transform, web_mercator, wgs84)

    # Generate random points (vertices) within the bounds
    vertices = []
    for _ in range(num_vertices):
        lat = round(random.uniform(min_lat, max_lat), 6)
        lon = round(random.uniform(min_lon, max_lon), 6)
        vertices.append((lon, lat))

    # Create a polygon from the random points
    polygon_wgs84 = Polygon(vertices)

    # Project polygon to Web Mercator and back to ensure it's valid
    polygon_web_mercator = transform(project_to_web_mercator, polygon_wgs84)
    wgs84_polygon = transform(project_to_wgs84, polygon_web_mercator)

    # Extract coordinates and convert to GeoJSON format
    exterior_coords = list(wgs84_polygon.exterior.coords)
    coords = [list(coord) for coord in exterior_coords]

    # Define properties (same as before)
    properties = CountryLightPollutionArea(
        name=f"{country_name} Light Pollution Area",
        radiance=round(random.uniform(10, 13), 2),
        satellite_source="VIIRS",
        date=datetime.now().strftime("%Y-%m-%d"),
    )

    # Return GeoFeature object with geometry and properties
    return GeoFeature(
        type="Feature",
        geometry={
            "type": "Polygon",
            "coordinates": [coords],  # GeoJSON expects a list of lists for polygons
        },
        properties=properties.dict(),
    )
