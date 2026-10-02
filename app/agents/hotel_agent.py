from app.state.user_response_state import User_Response_State
from app.tools.hotel_tools import search_hotel_tavily


def search_hotel_details(state: User_Response_State):
    response = search_hotel_tavily(state)
    return {
        "hotel_response": response["hotel_response"],
    }
