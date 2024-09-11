import random

from fastapi import APIRouter, HTTPException

from geo_api.models import GeoJSON
from geo_api.utils import generate_random_polygon_feature

router = APIRouter()


@router.get("/geojson")
async def get_geojson(country_name: str):
    feature = generate_random_polygon_feature(
        country_name, min_lat=50.0, max_lat=54.0, min_lon=3.0, max_lon=7.0
    )
    geo_data = GeoJSON(type="FeatureCollection", features=[feature])
    return {"data": geo_data}


@router.get("/geojson/{num_features}")
async def get_geojson_with_num_features(num_features: int = 10):
    if num_features <= 0:
        raise HTTPException(
            status_code=400, detail="Number of features must be positive"
        )

    countries = ["Netherlands", "Germany", "Belgium", "France"]

    geo_features = []
    for _ in range(num_features):
        country = random.choice(countries)
        feature = generate_random_polygon_feature(
            country, min_lat=50.0, max_lat=54.0, min_lon=3.0, max_lon=7.0
        )
        geo_features.append(feature)

    geo_data = GeoJSON(type="FeatureCollection", features=geo_features)
    return {"data": geo_data}
