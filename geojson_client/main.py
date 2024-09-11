import argparse
import json
from typing import Any, Dict

import requests


def fetch_geojson(country_name: str, base_url: str) -> Dict[str, Any]:
    url = f"{base_url}/geojson?country_name={country_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        json_data = response.json()

        if "data" not in json_data:
            raise KeyError("Expected 'data' key not found in the API response")

        return json_data["data"]

    except requests.RequestException as e:
        print(f"API request failed: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        raise
    except KeyError as e:
        print(f"Unexpected response structure: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="Fetch GeoJSON data for a country")
    parser.add_argument(
        "country_name", help="The name of the country to fetch data for"
    )
    parser.add_argument(
        "--base-url", default="http://localhost:8000", help="The base URL of the API"
    )

    args = parser.parse_args()

    print(f"Debug: country_name = {args.country_name}, base_url = {args.base_url}")

    try:
        geojson_data = fetch_geojson(args.country_name, args.base_url)

        feature = geojson_data["features"][0]
        properties = feature["properties"]
        geometry = feature["geometry"]

        print(f"Country: {args.country_name}")
        print(f"Name: {properties['name']}")
        print(f"Radiance: {properties['radiance']}")
        print(f"Satellite Source: {properties['satellite_source']}")
        print(f"Date: {properties['date']}")
        print(f"Geometry Type: {geometry['type']}")
        print(f"Number of Coordinates: {len(geometry['coordinates'][0])}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
