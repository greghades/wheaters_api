import os

from dotenv import load_dotenv
load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

WEATHER_API_URL = "https://api.openweathermap.org/data/3.0/onecall"
CITIES_API_URL = "https://search.reservamos.mx/api/v2/places"

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = os.getenv("REDIS_DB")