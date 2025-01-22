import requests
import pandas as pd
import matplotlib as plt
import Key

class WeatherClient:

    def __init__(self, city):
        self.city = city
        self.__actual = None
        self.__forecast = None

    def fetchActualData(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={Key.apiKey}=metric')
        try:
            response.raise_for_status()
            self.__actual = response
            print("Anfrage erfolgreich")
        except requests.exceptions.HTTPError as err:
            print(f"Ein Fehler ist aufgetreten: {err}") 

    def fetchForecastData(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={Key.apiKey}&units=metric')
        try:
            response.raise_for_status()
            self.__actual = response
            print("Anfrage erfolgreich")
        except requests.exceptions.HTTPError as err:
            print(f"Ein Fehler ist aufgetreten: {err}") 

    @property
    def dataDict(self):
        print(self.__response.json())   

    @property
    def status(self):
        pass

    def showWeather(self):
        pass

    def dataFrame(self):
        pass

    def plotData(self):
        pass

herford = WeatherClient("Herford")

herford.fetchData()
herford.dataDict

