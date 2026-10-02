from langchain_core.messages import HumanMessage
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from app.agents.flight_agent import flight_agent
from app.agents.hotel_agent import search_hotel_details
from app.nodes.extract_user_request import get_extract_user_information, validate_user_information
from app.state.user_response_state import User_Response_State

graph = StateGraph(User_Response_State)
graph.add_node("get_extract_user_information", get_extract_user_information)
graph.add_node("validate_user_information", validate_user_information)
graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", search_hotel_details)


graph.add_edge(START, "get_extract_user_information")
graph.add_edge("get_extract_user_information", "validate_user_information")
graph.add_edge("validate_user_information", "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")

graph.add_edge("hotel_agent", END)

app = graph.compile()

result = app.invoke({
    "user_message": "I want to travel from Launceston to Melbourne 2 adults and one child. I want to travel by flight on October 2, 2026, and return on October 2, 2026. My total budget is ₹50,000. Please find the available flights and help me plan the trip.",
    "messages": [
        HumanMessage(content="I want to travel from Launceston to Melbourne 2 adults and one child. I want to travel by flight on October 2, 2026, and return on October 2, 2026. My total budget is ₹50,000. Please find the available flights and help me plan the trip."),
    ]
})

print(result["hotel_response"])




