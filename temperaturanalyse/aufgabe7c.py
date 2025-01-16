import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import openmeteo_requests
import requests_cache
from retry_requests import retry
import datetime

class TemperatureChart:
    def __init__(self, latitude, longitude, start_date, end_date):
        # API Client setup
        self.cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
        self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
        self.openmeteo = openmeteo_requests.Client(session=self.retry_session)
        
        # Parameters for weather data request
        self.latitude = latitude
        self.longitude = longitude
        self.url = "https://archive-api.open-meteo.com/v1/archive"
        self.start_date = start_date
        self.end_date = end_date
        
        self.params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "hourly": "temperature_2m",
            "temporal_resolution": "hourly_6"
        }

        # Fetch the weather data
        self.responses = self.openmeteo.weather_api(self.url, params=self.params)
        self.response = self.responses[0]
        
        # Process the data
        self.process_hourly_data()

        # Define the weekday order
        self.weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def process_hourly_data(self):
        hourly = self.response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            )
        }
        
        hourly_data["temperature_2m"] = hourly_temperature_2m
        self.hourly_dataframe = pd.DataFrame(data=hourly_data)
        self.hourly_dataframe["date"] = pd.to_datetime(self.hourly_dataframe["date"], utc=True)

    def get_12pm_data(self):
        # Extract rows representing 12pm each day
        temperatures_12pm_per_weekday = self.hourly_dataframe[self.hourly_dataframe["date"].dt.hour == 12]

        # Add the weekdays to the data
        temperatures_12pm_per_weekday["weekday"] = temperatures_12pm_per_weekday["date"].dt.day_name()
        
        # Add the custom weekday order as categories
        temperatures_12pm_per_weekday['weekday'] = pd.Categorical(temperatures_12pm_per_weekday['weekday'], categories=self.weekday_order, ordered=True)

        return temperatures_12pm_per_weekday

    def get_current_week(self, temperatures_12pm_per_weekday):
        # Values of the current week
        end_date = temperatures_12pm_per_weekday.iloc[-1]
        end_date_weekday = end_date["weekday"]
        end_date_weekday_numeric = self.weekday_order.index(end_date_weekday)

        current_week = {
            "Monday": None,
            "Tuesday": None,
            "Wednesday": None,
            "Thursday": None,
            "Friday": None,
            "Saturday": None,
            "Sunday": None
        }
        
        # Iterate through the DataFrame backwards and fill the current_week dictionary
        for idx in range(7, -1, -1):
            weekday = temperatures_12pm_per_weekday.iloc[idx]["weekday"]
            weekday_numeric = self.weekday_order.index(weekday)

            if weekday_numeric <= end_date_weekday_numeric:
                current_week[weekday] = temperatures_12pm_per_weekday["temperature_2m"].iloc[idx]
        
        print(current_week)
        return current_week
    
    def calculate_stats(self, data):
        # Calculate mean, max, and min temperatures
        temperature_data_mean = data.groupby("weekday")["temperature_2m"].mean()
        temperature_data_max = data.groupby("weekday")["temperature_2m"].max()
        temperature_data_min = data.groupby("weekday")["temperature_2m"].min()

        return temperature_data_mean, temperature_data_max, temperature_data_min

    def create_chart(self, temperature_data_mean, temperature_data_max, temperature_data_min, current_week):
        # Create a plot
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot the mean temperature
        ax.plot(temperature_data_mean.index, temperature_data_mean.values, marker='o', label="Average Temperature", color='royalblue', linewidth=2)
        ax.plot(current_week.keys(), current_week.values(), marker='o', label="Current Week", color='orange', linewidth=2)

        # Scatter plot for max and min temperatures
        ax.scatter(temperature_data_max.index, temperature_data_max.values, color='darkred', label="Max Temperature", marker='^', s=100)
        ax.scatter(temperature_data_min.index, temperature_data_min.values, color='forestgreen', label="Min Temperature", marker='v', s=100)

        # Add axis labels and title
        ax.set_xlabel("Weekdays", fontsize=12, fontweight='bold', color='black')
        ax.set_ylabel("Temperature (°C)", fontsize=12, fontweight='bold', color='black')
        ax.set_title("Temperatures of the Week", fontsize=14, fontweight='bold', color='black')

        # Add gridlines
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

        # Set axis limits for better visualization
        ax.set_ylim([0, 20])

        # Add a legend
        ax.legend(loc='upper right')

        return fig

    def display_chart(self, fig):
        # Set up the Tkinter window
        root = tk.Tk()
        root.title("Temperature Chart")

        # Display the figure using Tkinter
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

        root.mainloop()

    def show_temperature_chart(self):
        # Get 12pm data
        temperatures_12pm_per_weekday = self.get_12pm_data()

        # Calculate the stats (mean, max, min)
        temperature_data_mean, temperature_data_max, temperature_data_min = self.calculate_stats(temperatures_12pm_per_weekday)
        current_week = self.get_current_week(temperatures_12pm_per_weekday)
        # Create the chart
        fig = self.create_chart(temperature_data_mean, temperature_data_max, temperature_data_min, current_week)

        # Display the chart
        self.display_chart(fig)

# Usage
start_date = datetime.date.today() - datetime.timedelta(days=70)
end_date = datetime.date.today()
chart = TemperatureChart(latitude=51.7667, longitude=7.95, start_date=start_date, end_date=end_date)
chart.show_temperature_chart()


