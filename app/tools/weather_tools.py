import requests

from app.config import get_open_weather_api_key, get_open_weather_api_url,get_open_weather_api_lat_log_url
from app.state.user_response_state import User_Response_State

open_weather_api_key = get_open_weather_api_key()
open_weather_api_lat_log_url = get_open_weather_api_lat_log_url()
open_weather_api_url = get_open_weather_api_url()

def get_open_weather_response(state: User_Response_State):
    location = state["destination"]
    params = {
        "appid": open_weather_api_key,
        "q": location,
        "limit": 1
    }
    response = requests.get(open_weather_api_lat_log_url, params=params)
    response.raise_for_status()

    response_json = response.json()

    response_lon = response_json[0]["lon"]
    response_lat = response_json[0]["lat"]

    weather_params = {
        "appid": open_weather_api_key,
        "lat": response_lat,
        "lon": response_lon,
        "units": "metric"
    }
    response_weather = requests.get(open_weather_api_url, params=weather_params)
    response_weather.raise_for_status()
    response_weather_json = response_weather.json()
    return response_weather_json




