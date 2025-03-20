import requests


def get_cities(slug_city:str)  :
    
    lugares = make_request(slug_city)
    coordenadas_ciudades = [
        lugares[i]
        for i in range(len(lugares))
        if lugares[i]["result_type"] == "city" and lugares[i]["country"] == "México"
    ]
    return coordenadas_ciudades


def make_request(slug: str) -> list:
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    url = f"https://search.reservamos.mx/api/v2/places?q={slug}"
    response = requests.get(url, headers=headers)

    if response.status_code == 201:
        return response.json()
    else:
        return []
