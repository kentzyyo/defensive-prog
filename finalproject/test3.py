#import the necessary libraries
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Create the main window
root=Tk()
root.title=("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Function to retrieve weather information
def getWeather():
    try:
        # Retrieve the city entered by the user
        city=textfield.get()
        
        # Initialize Geopy's Nominatim to fetch location details
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode(city)

        if location:
            # Get the full location name
            full_location_name = location.address  # Full location name including country
            print(f"{full_location_name}")

            # Fetch the timezone based on the coordinates
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            # Get current local time in the fetched timezone
            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M:%p")
            clock.config(text=current_time)
            name.config(text="STANDARD TIME")

            # Fetching current date
            current_date = local_time.strftime("%A, %B %d, %Y")
            date_label.config(text=current_date)
            
            # Fetch weather data using OpenWeatherMap API
            api_key="8138bf87612c86cbe7676267267eabc2" # Our OpenWeatherMap API
            api="http://api.openweathermap.org/data/2.5/weather?"
            complete_url = f"{api}q={city}&appid={api_key}&units=metric"

            json_data = requests.get(complete_url).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp'])
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']
            
            # Update GUI elements with weather information 
            t.config(text=(temp,"°C"))
            c.config(text=(condition,"|","FEELS","LIKE",temp,"°C"))
            w.config(text=(wind,"m/s"))
            h.config(text=(humidity,"%"))
            d.config(text=description)
            p.config(text=(pressure,"hPa"))

            location_label.config(text=f"Location: {full_location_name}")  # Display full location including country

        else:
            messagebox.showerror("Error", "Location not found")

    except Exception as e:
        messagebox.showerror("Invalid!")

#search box
Search_image=PhotoImage(file="finalproject\search.png")
myimage=Label(image=Search_image)
myimage.place(x=20, y=20)

textfield=tk.Entry(root,justify="center",width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon=PhotoImage(file="finalproject\search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

#logo
Logo_image=PhotoImage(file="finalproject\weatherIOS2.png")
logo=Label(image=Logo_image)
logo.place(x=600,y=100)

#Bottom box
Frame_image=PhotoImage(file="finalproject\lox.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#time
name=Label(root, font=("arial",15,"bold"))
name.place(x=30, y=100)
clock=Label(root, font=("Helvetica",15))
clock.place(x=30, y=130)
date_label= Label(root, font=("Helvetica", 15))
date_label.place(x=30, y=160)  # Adjust the coordinates as needed

#place
location_label = Label(root, font=("Helvetica", 15))
location_label.place(x=30, y=190)  # Adjust the coordinates as needed

#label
label1=Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2=Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3=Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4=Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial", 70, 'bold'),fg="#ee666d")
t.place(x=100, y=220)

c=Label(font=("arial", 15, 'bold'))
c.place(x=100, y=335)

w=Label(text="", font=("arial", 20, 'bold'), bg="#1ab5ef")
w.place(x=120, y=430)
h=Label(text="", font=("arial", 20, 'bold'), bg="#1ab5ef")
h.place(x=280, y=430)
d=Label(text="", font=("arial", 20, 'bold'), bg="#1ab5ef")
d.place(x=430, y=430)
p=Label(text="", font=("arial", 20, 'bold'), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()