from app.state.user_response_state import User_Response_State
from app.tools.weather_tools import get_open_weather_response


def get_weather_agent(state: User_Response_State):
    response = get_open_weather_response(state)
    return {
        "hotel_response": response,
    }