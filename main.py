from langchain_core.messages import HumanMessage
from langchain_mcp_adapters import tools
from langgraph.constants import START, END
from langgraph.graph import StateGraph
from langgraph.types import Send

from app.agents.flight_agent import flight_agent
from app.agents.hotel_agent import search_hotel_details
from app.agents.itinerary_agent import itinerary_agent_call
from app.agents.supervisor_agent import supervisor_agent
from app.agents.weather_agent import get_weather_agent
from app.nodes.extract_user_request import get_extract_user_information, validate_user_information
from app.state.user_response_state import User_Response_State

graph = StateGraph(User_Response_State)
graph.add_node("supervisor_agent", supervisor_agent)
graph.add_node("get_extract_user_information", get_extract_user_information)
graph.add_node("validate_user_information", validate_user_information)
graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", search_hotel_details)
graph.add_node("weather_agent", get_weather_agent)
graph.add_node("itinerary_agent_call", itinerary_agent_call)

graph.add_edge(START, "get_extract_user_information")
graph.add_edge("get_extract_user_information", "validate_user_information")

graph.add_edge("validate_user_information", "supervisor_agent")


def route_agents(state: User_Response_State):
    selected_agents = state["selected_agents"]

    node_map = {
        "FlightAgent": "flight_agent",
        "HotelAgent": "hotel_agent",
        "WeatherAgent": "weather_agent",
    }

    return [Send(node_map[a], state) for a in selected_agents]

graph.add_conditional_edges("supervisor_agent", route_agents, {
    "FlightAgent": "flight_agent",
    "HotelAgent": "hotel_agent",
    "WeatherAgent": "weather_agent"
})

graph.add_edge("flight_agent", "itinerary_agent_call")
graph.add_edge("hotel_agent", "itinerary_agent_call")
graph.add_edge("weather_agent", "itinerary_agent_call")

graph.add_edge("itinerary_agent_call", END)


# graph.add_edge("validate_user_information", "flight_agent")
# graph.add_edge("validate_user_information", "hotel_agent")
# graph.add_edge("validate_user_information", "weather_agent")
# #graph.add_edge("weather_agent", END)
# graph.add_edge("flight_agent", "supervisor_agent")
# graph.add_edge("hotel_agent", "supervisor_agent")
# graph.add_edge("weather_agent", "supervisor_agent")
#
# graph.add_edge("supervisor_agent", END)

app = graph.compile()

result = app.invoke({
    "user_message": "I want to travel from Launceston to Melbourne 2 adults and one child. I want to travel by flight on October 2, 2026, and return on October 2, 2026. My total budget is ₹50,000. Please find the available flights and help me plan the trip.",
    "messages": [
        HumanMessage(content="I want to travel from Launceston to Melbourne 2 adults and one child. Provide the hotel details as well as weather I want to travel by flight on October 2, 2026, and return on October 2, 2026. My total budget is ₹50,000. Please find the available flights and help me plan the trip."),
    ]
})

# print("============================================= Hotel Response ==================================")
# print(result["hotel_response"])
# print("============================================= Flight Response ==================================")
# print(result["flight_response"])
# print("============================================= Weather Response ==================================")
# print(result["weather_response"])




