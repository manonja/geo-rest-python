from typing import Any, Dict

from pydantic import BaseModel


class GeoInfoRequest(BaseModel):
    geojson_polygon: Dict[str, Any]
    geographic_data: str

    class Config:
        schema_extra = {
            "example": {
                "geojson_polygon": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [-122.4, 37.7],
                            [-122.4, 37.8],
                            [-122.5, 37.8],
                            [-122.5, 37.7],
                            [-122.4, 37.7],
                        ]
                    ],
                },
                "geographic_data": "encoded_string_of_geographic_data",
            }
        }
