import requests
from config import WEATHER_API_KEY
from utils.icons import weather_icons

def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url).json()
    if response.get("cod") != 200:
        return "Не удалось найти город"
    temp = response["main"]["temp"]
    condition = response["weather"][0]["main"]

    desc = response["weather"][0]["description"]

    icon = weather_icons.get(condition, "🌍")

    return f"🌡 Температура в городе {city}: {temp}°C\n{icon} Погода в городе {city}: {desc.capitalize()}"
