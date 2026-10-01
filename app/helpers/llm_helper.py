import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

from app.config import get_anthropic_api_key, get_anthropic_model_name

load_dotenv(verbose=True)



def get_llm():
    try:
        llm = ChatAnthropic(
            api_key=get_anthropic_api_key(),
            model_name=get_anthropic_model_name())
        return { "chat_model": llm, "is_success": True }
    except Exception as e:
        return { "error_message": e.message, "is_success": False }

def get_llm_content(prompt: str):
    try:
        llm = get_llm()
        if llm["is_success"]:
            content = llm["chat_model"].invoke(prompt)
            return {"content": content.content, "is_success": True}
        else:
            return {"error_message": llm["error_message"], "is_success": False}
    except Exception as e:
        return {"error_message": e.message, "is_success": False}
