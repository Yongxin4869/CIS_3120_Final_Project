import matplotlib.pyplot as plt      #Import the matplot library to prepare draw graphs.

class Visualization:
    
    def one_day_temp(self, weather_data):          # It will show 24 hours temperature. Get 
        temperatures = []                          # Use for loop to put all the information in [ ], then use that to draw graph
        time = []
        for day in weather_data['days']:
            for hour_data in day['hours']:
                temperatures.append(hour_data['temp'])
                time.append(hour_data['datetime'])
        
        plt.figure(figsize=(10, 6))
        plt.plot(time, temperatures)
        plt.xlabel('Hours')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature changes')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

    def one_day_condition(self, weather_data):         #This one is similar than the above one. This one is a bar graph.
        conditions = []                                #It will display that day's condition. So people can decide what they should bring with them.
        time = []                                      #For example, Rainy day, you should bring an umbrella. 
        for day in weather_data['days']:
            for hour_condition in day['hours']:
                conditions.append(hour_condition['conditions'])
                time.append(hour_condition['datetime'])
        
        plt.figure(figsize=(10, 6))
        
        plt.bar(time, conditions)
        plt.xlabel('Hours')
        plt.ylabel('Conditions')
        plt.title('Weather conditions')
        plt.xticks(rotation=45)
        plt.show()

