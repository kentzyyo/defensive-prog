import requests
from tkinter import Tk, Label, Entry, Button, messagebox
from geopy.geocoders import Nominatim

def get_weather(city):
    api_key = "8138bf87612c86cbe7676267267eabc2"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if response.status_code == 200:
        city_name = data["name"]
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_info = f"Weather in {city_name}: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Error", "Error fetching weather data. Please try again later.")

def get_location_autocomplete(query):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(query)
    if location:
        location_info = f"Location: {location.address}\nLatitude: {location.latitude}, Longitude: {location.longitude}"
        messagebox.showinfo("Location Details", location_info)
    else:
        messagebox.showerror("Error", "Location not found. Please enter a valid location.")

def fetch_weather():
    city_input = entry_city.get()
    get_weather(city_input)

def fetch_location():
    location_input = entry_location.get()
    get_location_autocomplete(location_input)

# Create GUI window
root = Tk()
root.title("Weather App")

# Create and place widgets
label_city = Label(root, text="Enter city name:")
label_city.pack()
entry_city = Entry(root)
entry_city.pack()

button_weather = Button(root, text="Get Weather", command=fetch_weather)
button_weather.pack()

label_location = Label(root, text="Enter location:")
label_location.pack()
entry_location = Entry(root)
entry_location.pack()

button_location = Button(root, text="Get Location Details", command=fetch_location)
button_location.pack()

root.mainloop()
