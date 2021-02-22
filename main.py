import requests
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable


def get_followers(screen_name: str, token: str, count: str) -> dict:
    """
    This function returns a json object with information about followers
    of a person with the given screen_name.
    """
    base_url = "https://api.twitter.com/"


    search_url = "{}1.1/friends/list.json".format(base_url)

    search_headers = {
        'Authorization': 'Bearer {}'.format(token)
    }

    search_params = {
        'screen_name': f"{screen_name}",
        'count': int(count)
    }

    response = requests.get(
        search_url, headers=search_headers, params=search_params)

    json_response = response.json()

    return json_response


def get_locations(data: dict) -> dict:
    """
    This function takes in a list of followers as a dictionary and forms a new
    dictionary with screen_name-location pairs.
    """
    locations = {}
    for i in data["users"]:
        key = i["name"]
        value = i["location"]
        if value != '':
            locations[key] = value
    return locations


def coordinates(place: str) -> tuple:
    """
    This function calculates coordinates
    of the places on the given dictionary.
    """
    try:
        geolocator = Nominatim(user_agent="Followers-Map")
        location = geolocator.geocode(place)
        if hasattr(location, 'latitude') and location.latitude is not None:
            if hasattr(location, 'longitude') and location.longitude is not None:
                return ((location.latitude, location.longitude), place)
        return 'Not found'
    except:
        'GeocoderUnavailable'


def processing_locations(locations):
    """
    This function takes in a dictionary with follower-location pairs,
    adds coordinates, if possible, and deletes a pair if coordinates are not found.
    """
    new_locations = []
    for place in locations:
        coords = coordinates(locations[place])
        if "Not found" not in coords:
            new_locations.append((place, coords))
    return new_locations


def create_map(locations):
    """
    This function creates a map with the followers locations on it.
    """
    geomap = folium.Map(zoom_start=15)
    fg_1 = folium.FeatureGroup(name="Followers")
    fg_2 = folium.FeatureGroup(name="Places", show=False)
    for i in range(len(locations)):
        rec = locations[i][1]
        coords, name = rec[0], locations[i][0]
        lat, lon = coords[0], coords[1]
        place = rec[1]
        fg_1.add_child(folium.Marker(
            location=[lat, lon], popup=name, icon=folium.Icon(color='lightgreen')))
        fg_2.add_child(folium.Marker(
            location=[lat, lon], popup=place, icon=folium.Icon(color='gray')))
    geomap.add_child(fg_1)
    geomap.add_child(fg_2)
    folium.LayerControl().add_to(geomap)
    geomap.save("templates/some.html")
