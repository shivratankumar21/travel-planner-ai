from app.state.user_response_state import User_Response_State
from app.tools.hotel_tools import search_hotel_tavily


def search_hotel_details(state: User_Response_State):
    print("search_hotel_tavily")
    response = search_hotel_tavily(state)
    print(response)
    if response["is_success"] == True:
        return {
            "hotel_response": response["hotel_response"],
        }
    else:
        return state
