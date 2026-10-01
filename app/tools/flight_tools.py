import requests

from app.config import get_aviation_stack_key,get_aviation_stack_api_url
from app.helpers.city_code import get_city_code_by_name
from app.state.user_response_state import User_Response_State

aviation_stack_api_key = get_aviation_stack_key()
aviation_stack_api_url = get_aviation_stack_api_url()


def search_flight_details(state: User_Response_State):
    start_date = state["start_date"]
    source = state["source"]
    destination = state["destination"]

    source_city_code = get_city_code_by_name(source)
    destination_city_code = get_city_code_by_name(destination)
    params = {
        "access_key": aviation_stack_api_key
    }

    print(f"Source : {source_city_code}, Destination : {destination_city_code}, Start Date: {start_date}")

    response = requests.get(aviation_stack_api_url, params=params)
    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        flight_details = data.get("data",[])
        filtered_flights = []

        for flight in flight_details:
            if (
                    flight.get("flight_date") == start_date
                    and flight.get("departure", {}).get("iata", "").upper() == source_city_code.upper()
                    and flight.get("arrival", {}).get("iata", "").upper() == destination_city_code.upper()
            ):
                filtered_flights.append(flight)

        return flight_details
    else:
        return []

