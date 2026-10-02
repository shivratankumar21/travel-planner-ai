from tavily import TavilyClient

from app.state.user_response_state import User_Response_State
from app.config import get_tavily_api_key

tavily_api_key = get_tavily_api_key()

def search_hotel_tavily(state: User_Response_State):
    destination = state["destination"]
    start_date = state["start_date"]
    end_date = state["end_date"]
    adults = state["adults"]
    children = state["children"]
    prompt_message = (
        f"Find hotels in {destination} from {start_date} to {end_date} "
        f"for {adults} adults and {children} children. "
        f"Include price, room type, rating, amenities, cancellation, "
        f"breakfast, availability and booking URL."
    )
    try:
        tavily_client = TavilyClient(api_key= tavily_api_key)
        response = tavily_client.search(query=prompt_message)
        return {"hotel_response": response["results"], "is_success": True}
    except Exception as e:
        return {"hotel_response": [], "is_success": False}

