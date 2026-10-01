from typing import TypedDict, Optional


class UserRequestState(TypedDict):
    user_message: str
    username: Optional[str]
    source: Optional[str]
    destination: Optional[str]
    start_date: Optional[str]
    end_date: Optional[str]
    adults: Optional[int]
    children: Optional[str]
    travel_mode: Optional[str]
    missing_fields: Optional[str]
    budget: Optional[float ]
    

