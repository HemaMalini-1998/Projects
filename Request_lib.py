#pip install requests
import requests

# Replace with your OpenWeatherMap API key
api_key ="bf24ec2207e8bf903524c4278eb67c83"
latitude = 12.9048 # Replace with the latitude of your district
longitude = 80.0891 # Replace with the longitude of your district

# Create the API URL with the latitude and longitude
url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

# Send an HTTP GET request to the API
response = requests.get(url)

if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract relevant weather information
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    city_name = data["name"]

    # Display the weather information
##    print(data)
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature} K")
    print(f"Description: {weather_description}")
else:
    print("Error fetching weather data. Please check the coordinates or your API key.")
