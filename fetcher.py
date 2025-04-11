import os

def get_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()
