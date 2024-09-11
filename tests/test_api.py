from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_geojson_netherlands():
    response = client.get("/geojson?country_name=Netherlands")
    assert response.status_code == 200
    data = response.json()

    assert "data" in data
    geojson = data["data"]

    assert geojson["type"] == "FeatureCollection"
    assert len(geojson["features"]) > 0

    feature = geojson["features"][0]
    assert feature["type"] == "Feature"
    assert "geometry" in feature
    assert "properties" in feature

    properties = feature["properties"]
    assert properties["name"] == "Netherlands Light Pollution Area"
    assert "radiance" in properties
    assert "satellite_source" in properties
    assert "date" in properties


def test_get_geojson_invalid_country():
    response = client.get("/geojson?country_name=InvalidCountry")
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Country not found"
