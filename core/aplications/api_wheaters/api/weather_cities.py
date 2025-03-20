import requests



# Obtener la temperatura maxima y minima de las ciudades
def get_weather(cities: list = []):
    weather = []
    for i in range(len(cities)):
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={cities[i]["lat"]}&lon={cities[i]["long"]}&exclude=current,minutely,hourly,alerts&appid=0fab674fe64a90917ccdef9fa9a947e0"
        response = requests.get(url)
        if response.status_code == 200:
            weather.append(response.json())
    return weather


# Devolver la lista de las ciudades con sus coordenadas y temperatura maxima y minima
def get_cities_and_temp(cities):
    weather = get_weather(cities)

    for i in range(len(weather)):

        daily_temp = weather[i]["daily"]

        max_temps_daily = []
        min_temps_daily = []

        # Obtener las temperaturas maxima y minima de cada dia
        for j in range(len(daily_temp)):
            max_temps_daily.append(daily_temp[j]["temp"]["max"])
            min_temps_daily.append(daily_temp[j]["temp"]["min"])

        # Asignar tener la temperatura maxima y minima de la ciudad
        cities[i]["max_temps_daily"] = max(max_temps_daily)
        cities[i]["min_temps_daily"] = min(max_temps_daily)

    return cities
