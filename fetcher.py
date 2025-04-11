def get_weather(city):
    try:
        response = requests.get(f"https://api.weatherapi.com/v1/current.json?q={city}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch weather: {e}")
        return {}
