from typing import TypedDict, Annotated, Optional, Any

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class User_Response_State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    is_missing_field: bool
    user_message: str
    flight_response: list[dict[str, Any]]
    train_response: list[dict[str, Any]]
    hotel_response: list[dict[str, Any]]
    weather_response: list[dict[str, Any]]
    itinerary_response: list[dict[str, Any]]
    budgest_response: list[dict[str, Any]]
    username: Optional[str]
    source: Optional[str]
    destination: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    adults: Optional[int]
    children: Optional[str]
    travel_mode: Optional[str]
    missing_fields: Optional[str]
    budget: Optional[float]
    llm_call_counter : Optional[int]



