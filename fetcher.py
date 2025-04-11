import requests

def get_weather(city):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?q={city}")
    return response.json()

def is_rainy(weather_data):
    return "rain" in weather_data["current"]["condition"]["text"].lower()
