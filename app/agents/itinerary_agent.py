from app.state.user_response_state import User_Response_State


def  itinerary_agent_call(state: User_Response_State):
    print("itinerary agent agent called")
    return {
        "itinerary_response": "[]"
    }