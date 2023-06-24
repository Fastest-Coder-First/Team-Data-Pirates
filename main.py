import requests
from datetime import datetime

def fetch_weather(city_name):
    # Construct the URL for weather data using the city name and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=c9d3180a526ee27861dc136b4508ff4f"
    
    # Send a GET request to the API endpoint
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the weather data in JSON format
        return response.json()
    else:
        # Raise an exception with the corresponding error message
        raise Exception(f"Error fetching weather data. Status code: {response.status_code}")

def display_weather(weather_data):
    # Extract relevant information from the weather data using nested dictionary access
    location = weather_data['coord']['lon'], weather_data['coord']['lat']
    sunrise = weather_data['sys']['sunrise']
    sunset = weather_data['sys']['sunset']
    main_weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    visibility = weather_data['visibility']
    cloudiness = weather_data['clouds']['all']
    rain = weather_data.get('rain', {}).get('1h', 0)
    snow = weather_data.get('snow', {}).get('1h', 0)

    # Convert sunrise and sunset timestamps to human-readable format in UTC
    sunrise_time = datetime.utcfromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S')
    sunset_time = datetime.utcfromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S')

    # Display the weather forecast
    print(f"City: {weather_data['name']}, {weather_data['sys']['country']}")
    print(f"Longitude: {location[0]}, Latitude: {location[1]}")
    print(f"Sunrise: {sunrise_time} UTC")
    print(f"Sunset: {sunset_time} UTC")
    print(f"Weather: {main_weather}, more precisely {description}")
    print(f"Temperature: {temperature} K or {round(temperature - 273.15, 2)}° C")
    print(f"Feels like: {feels_like} K or {round(feels_like - 273.15, 2)}° C")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Visibility: {visibility} meters")
    print(f"Cloudiness: {cloudiness}%")
    print(f"Rain (last 1 hour): {rain} mm")
    print(f"Snow (last 1 hour): {snow} mm")

try:
    # Prompt the user to enter a city name
    city_name = input("Enter desired city name: ")
    
    # Fetch the weather data for the specified city
    weather_data = fetch_weather(city_name)
    
    # Display the weather forecast
    display_weather(weather_data)
    
    # Fetch and print additional weather information from a different source
    url = "https://wttr.in/{}".format(city_name)
    res = requests.get(url)
    print("Here is the weather forecast of the city you requested: ")
    print(res.text)
    
except Exception as e:
    # Handle exceptions and display error messages
    print(e)
    print("Error fetching weather data. Please try again later.")
