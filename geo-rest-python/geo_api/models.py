from typing import List

from pydantic import BaseModel


class GeoJSONFeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: List[dict] = []
