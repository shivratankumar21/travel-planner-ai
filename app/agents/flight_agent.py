from app.state.user_response_state import User_Response_State
from app.tools.flight_tools import search_flight_details


def flight_agent(state: User_Response_State):
    print("flight_agent is called")
    response_flight_details = search_flight_details(state)
    return { "flight_response": response_flight_details }

