import requests


def fetch_weather(api_key, location):
    """Fetches current weather data for a specified location using the WeatherAPI."""
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Failed to fetch weather data: {error}")
        return None

def display_weather(weather_data):
    """Displays the weather data in a user-friendly format."""
    if not weather_data:
        print("No weather data available.")
        return

    location = weather_data.get("location", {})
    current = weather_data.get("current", {})

    print("\n--- Weather Information ---")
    print(f"Location: {location.get('name')}, {location.get('country')}")
    print(f"Local Time: {location.get('localtime')}")
    print(f"Condition: {current.get('condition', {}).get('text')}")
    print(f"Temperature: {current.get('temp_c')}°C ({current.get('temp_f')}°F)")
    print(f"Feels Like: {current.get('feelslike_c')}°C ({current.get('feelslike_f')}°F)")
    print(f"Wind: {current.get('wind_kph')} km/h ({current.get('wind_mph')} mph), {current.get('wind_dir')}")
    print(f"Humidity: {current.get('humidity')}%")
    print(f"Cloud Cover: {current.get('cloud')}%")
    print("---------------------------\n")

def main():
    api_key = "edd4722a24eb4dca8d2161132241901"
    location = input("Enter the city name: ")
    weather_data = fetch_weather(api_key, location)

    if weather_data:
        display_weather(weather_data)


if __name__ == "__main__":
    main()