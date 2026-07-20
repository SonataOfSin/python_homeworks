#ჯერ უნდა გვქონდეს დაინსტალირებული requests მოდული
# ტერმინალში pip install requests

import requests

def get_weather():
    # 1. მომხმარებლისგან ქალაქის სახელის მიღება
    city_name = input("Enter city name: ")

    # API 1 — Geocoding API
    geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city_name,
        "count": 1
    }

    try:
        # მოთხოვნის გაგზავნა Geocoding API-ზე
        geo_response = requests.get(geocoding_url, params=geo_params)
        geo_response.raise_for_status() # ამოწმებს HTTP შეცდომებს
        geo_data = geo_response.json()

        # ვამოწმებთ, მოიძებნა თუ არა ქალაქი
        if "results" not in geo_data or len(geo_data["results"]) == 0:
            print("City not found")
            return

        # კოორდინატების და ქალაქის ზუსტი სახელის ამოღება
        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        found_city_name = location["name"]

        # API 2 — Weather Forecast API
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,wind_speed_10m",
            "timezone": "auto"
        }

        # მოთხოვნის გაგზავნა ამინდის API-ზე
        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # მიმდინარე ამინდის მონაცემების ამოღება
        current = weather_data["current"]
        temperature = current["temperature_2m"]
        wind_speed = current["wind_speed_10m"]
        time = current["time"]

        # საბოლოო შედეგის დაბეჭდვა მოთხოვნილი ფორმატით
        print(f"City: {found_city_name}")
        print(f"Temperature: {temperature} °C")
        print(f"Wind Speed: {wind_speed} km/h")
        print(f"Time: {time}")

    except requests.exceptions.RequestException as e:
         # იჭერს ინტერნეტთან ან სერვერთან დაკავშირებულ ნებისმიერ შეცდომას (პროგრამა არ იქრაშება)
        print("Network error or API is unavailable.")

if __name__ == "__main__":
    get_weather()
