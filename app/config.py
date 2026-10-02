import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_aviation_stack_key():
    return os.getenv("AVIATION_STACK_API_KEY")

def get_aviation_stack_api_url():
    return os.getenv("AVIATION_STACK_URL")

def get_anthropic_api_key():
    return os.getenv("ANTHROPIC_API_KEY")

def get_anthropic_model_name():
    return os.getenv("ANTHROPIC_MODEL_NAME")

def get_tavily_api_key():
    return os.getenv("TAVILY_API_KEY")

def get_open_weather_api_key():
    return os.getenv("OPEN_WEATHER_API_KEY")

def get_open_weather_api_lat_log_url():
    return os.getenv("OPEN_WEATHER_API_LAT_LON_URL")

def get_open_weather_api_url():
    return os.getenv("OPEN_WEATHER_API_URL")


