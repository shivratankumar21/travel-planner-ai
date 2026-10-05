from app.state.user_response_state import User_Response_State
from app.tools.weather_tools import get_open_weather_response


def get_weather_agent(state: User_Response_State):
    print("Weather Agent Started")
    response = get_open_weather_response(state)
    return {
        "weather_response": response,
    }