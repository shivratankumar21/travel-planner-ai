from langchain_core.messages import HumanMessage
from langgraph.constants import START, END
from langgraph.graph import StateGraph

from app.nodes.extract_user_request import get_extract_user_information, validate_user_information
from app.state.user_response_state import User_Response_State

graph = StateGraph(User_Response_State)
graph.add_node("get_extract_user_information", get_extract_user_information)
graph.add_node("validate_user_information", validate_user_information)

graph.add_edge(START, "get_extract_user_information")
graph.add_edge("get_extract_user_information", "validate_user_information")

graph.add_edge("validate_user_information", END)

app = graph.compile()

result = app.invoke({
    "user_message": "I want to travel from Bangalore to Goa",
    "messages": [
        HumanMessage(content="I want to travel from Bangalore to Goa"),
    ]
})

print(result["messages"][-1].content)
