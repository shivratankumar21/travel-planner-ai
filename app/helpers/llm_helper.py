import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv(verbose=True)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL_NAME = os.getenv("ANTHROPIC_MODEL_NAME")

def get_llm():
    try:
        llm = ChatAnthropic(
            api_key=ANTHROPIC_API_KEY,
            model_name=ANTHROPIC_MODEL_NAME)
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
