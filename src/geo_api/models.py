from typing import List, Optional

from pydantic import BaseModel


# Single feature in GeoJSON format
class GeoFeature(BaseModel):
    type: str
    geometry: dict
    properties: Optional[dict] = None


# Overall GeoJSON structure
class GeoJSON(BaseModel):
    type: str
    features: List[GeoFeature]


# Wraps our GeoJSON data for consistency in API responses
class GeoData(BaseModel):
    geojson: GeoJSON


class CountryLightPollutionArea(BaseModel):
    name: str
    radiance: float
    satellite_source: str
    date: str
