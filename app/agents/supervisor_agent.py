import json

from langgraph.graph import state

from app.helpers.llm_helper import get_llm_content
from app.state.user_response_state import User_Response_State


def get_agents_for_supervisor(user_query):

    PROMPT_SUPERVISOR_AGENT = f"""
                You are the Supervisor Agent responsible for coordinating a travel planning workflow.

            Your job is to analyze the user's request and decide which specialized agents are required to fulfill the request.

            Available agents:

            1. FlightAgent
               - Searches and provides flight information.
               - Use this agent when the user asks about flights, airlines, departure/arrival information, or flight availability.

            2. HotelAgent
               - Searches and provides hotel information.
               - Use this agent when the user asks about hotels, accommodation, rooms, or hotel availability.

            3. WeatherAgent
               - Provides weather information for the requested destination.
               - Use this agent when the user asks about weather, temperature, forecast, rain, or climate.

            # 4. FinalAgent
            #    - Combines the results from the selected agents and generates the final response to the user.
            #    - FinalAgent should be called only after all required specialized agents have completed their work.

            Your responsibilities:

            - Understand the user's request.
            - Identify all specialized agents required to fulfill the request.
            - You may select multiple agents when the request requires multiple types of information.
            - Do not select agents that are not required.
            - Do not perform the actual flight, hotel, or weather task yourself.
            - Return the names of the required specialized agents.

            # Examples:
            # 
            # User:
            # "Find me a flight from Bangalore to London."
            # 
            # Output:
            # ["FlightAgent"]

            User:
            "Find me a flight and hotel in London."

            Output:
            ["FlightAgent", "HotelAgent"]

            User:
            "I am travelling to London. Find me a flight, hotel and tell me the weather."

            Output:
            ["FlightAgent", "HotelAgent", "WeatherAgent"]

            User:
            "What is the weather in London?"

            Output:
            ["WeatherAgent"]

            The workflow will execute the selected agents and then pass their results to FinalAgent.
            User Request: 
            {user_query}
    """
    return PROMPT_SUPERVISOR_AGENT;


def supervisor_agent(state: User_Response_State):
    response = get_llm_content(get_agents_for_supervisor(state["messages"]))
    response_json = json.loads(response["content"])
    return {
        "selected_agents": response_json
    }
