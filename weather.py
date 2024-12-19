#Import everything that we need.
import requests
import matplotlib.pyplot as plt
from key import API_KEY     #Import my API_KEY from another file
import pandas as pd


class weather:
    def __init__(self, location, date):  # Location and date are mandatory
        self.location = location
        self.temperature = None  # Placeholder for temperature.
        self.date = date
        self.url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{self.location}/{self.date}?unitGroup=metric&key={API_KEY}&contentType=json"
        self.data = None  # Placeholder for the weather data.

    def current_location(self):       #Tells you the current location
        return f"This is the weather result for {self.location}."

    def current_temperature(self):    #Tells you the current temperature
        return f"The current temperature is {self.temperature}"

    def current_date(self):          #Tells you the current date
        return f"This is the latest data. It was the data of {self.date}"

    def __str__(self):             #Sum up everything above. Use their information to generate sentences / information.
        return f"Location:{self.location}\nDate:{self.date}\nToday's Average Temperature:{self.temperature}"

    # To get the basic data from the API link. This is the most important part in this project.
    def weather_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()

            # It has multiple days under the "days" object, so I only call the 1st one which represents the current time.
            self.temperature = data["days"][0]["temp"]
            self.date = data["days"][0]["datetime"]
            self.data = data  # Save the data
        else:
            return "Oops! It looks like something went wrong! Please try again later!"
        return data      #Make sure others also can use it.

    # It will show 24 hours temperature.
    def one_day_temp(self): 
        temperatures = []  # Use for loop to put all the information in [], then use that to draw graph
        time = []
        for day in self.data['days']:
            for hour_data in day['hours']:
                temperatures.append(hour_data['temp'])
                time.append(hour_data['datetime'])
        
        plt.figure(figsize=(10, 6))
        plt.plot(time, temperatures)
        plt.xlabel('Hours')
        plt.ylabel('Temperature (°C)')
        plt.title(f'Temperature changes in {self.location}')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

    # This one is similar than the above one. This one is a bar graph.
    def one_day_condition(self):  
        conditions = []  # It will display that day's condition. So people can decide what they should bring with them.
        time = []  # For example, Rainy day, you should bring an umbrella.
        for day in self.data['days']:
            for hour_condition in day['hours']:
                conditions.append(hour_condition['conditions'])
                time.append(hour_condition['datetime'])
        
        plt.figure(figsize=(10, 6))
        plt.bar(time, conditions)
        plt.xlabel('Hours')
        plt.ylabel('Conditions')
        plt.title(f'Weather conditions in {self.location}')
        plt.xticks(rotation=45)
        plt.show()


#Testing 
washington = weather('Washington', '2024-12-18')  #Give the basic information
washington.weather_data()        # Get basic information
washington.one_day_temp()        # Line graph
washington.one_day_condition()    # bar graph
