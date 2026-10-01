import json

from app.helpers.llm_helper import get_llm_content
from app.prompts.extract_user_response import get_prompt_content
from app.state.user_response_state import User_Response_State


def get_extract_user_information(state: User_Response_State):
    user_request = state["user_message"]

    user_system_prompt = get_prompt_content(user_request)
    extract_response = get_llm_content(user_system_prompt)

    if extract_response["is_success"] == True:
        extract_response = extract_response["content"]
        extract_response = extract_response.replace("```json", "").replace("```", "").strip()
        extract_response = json.loads(extract_response)
        return {
            "source": extract_response["source"],
            "destination": extract_response["destination"],
            "start_date": extract_response["start_date"],
            "end_date": extract_response["end_date"],
            "adults": extract_response["adults"],
            "children": extract_response["children"],
            "travel_mode": extract_response["travel_mode"],
            "budget": extract_response["budget"],
        }
    return state

def validate_user_information(state: User_Response_State):
    list_of_missing_fields = []

    if state["source"] is None:
        list_of_missing_fields.append("source")

    if state["destination"] is None:
        list_of_missing_fields.append("destination")

    if state["start_date"] is None:
        list_of_missing_fields.append("start_date")

    if state["end_date"] is None:
        list_of_missing_fields.append("end_date")

    if state["adults"] is None:
        list_of_missing_fields.append("adults")

    return {
        "missing_fields": ", ".join(list_of_missing_fields)
    }





