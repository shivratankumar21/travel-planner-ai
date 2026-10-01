from typing import TypedDict, Annotated, Optional

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages

class User_Response_State(TypedDict):
    messages: Annotated[dict[AnyMessage], add_messages]
    is_missing_field: bool
    user_message: str
    flight_response: list[str]
    train_response: list[str]
    hotel_response: list[str]
    weather_response: list[str]
    itinerary_response: list[str]
    budgest_response: list[str]
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



