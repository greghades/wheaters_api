import requests
from config import (
    WEATHER_API_KEY,
    WEATHER_API_URL,
    CITIES_API_URL,
    # REDIS_HOST,
    # REDIS_PORT,
    # REDIS_PASSWORD,
    # REDIS_DB,
)

# Obtener la temperatura maxima y minima de las ciudades
def fetch_weather_api(cities: list = []):

    weather = []
    
    for city in cities:
        # url = f"https://api.openweathermap.org/data/3.0/onecall?lat={city["lat"]}&lon={city["long"]}&exclude=current,minutely,hourly,alerts&appid=0fab674fe64a90917ccdef9fa9a947e0"
        params = {
            "lat":city["lat"],
            "lon":city["long"],
            "exclude":"current,minutely,hourly,alerts",
            "appid":WEATHER_API_KEY
        }
        
        try:
            response = requests.get(WEATHER_API_URL,params=params)
            response.raise_for_status()
            weather.append(response.json())     

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return None
                
    return weather


# Devolver la lista de las ciudades con sus coordenadas y temperatura maxima y minima
def get_wheater_data(cities):

    weather = fetch_weather_api(cities)

    for i,item in enumerate(weather):

        daily_temp = item["daily"]

        max_temps_daily = [temp["temp"]["max"] for temp in daily_temp]
        min_temps_daily = [temp["temp"]["min"] for temp in daily_temp]
        
        temp_over_seven_days = {
            "max":max(max_temps_daily),
            "min":min(min_temps_daily)
        }
        # Asignar tener la temperatura maxima y minima de la ciudad
        cities[i]["temp_over_seven_days"] = temp_over_seven_days
    
    return cities


def get_cities_data(slug_city:str)  :
    
    lugares = fetch_cities_api(slug_city)
    cities = [
        lugar for lugar in lugares
        if lugar["result_type"] == "city" and lugar["country"] == "México"
    ]
    return cities

def fetch_cities_api(slug: str) -> list:
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {"q":slug}

    try:
        response = requests.get(CITIES_API_URL, headers=headers,params=params)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data {e}")
        return None
 
    return response.json()