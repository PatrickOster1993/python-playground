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
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={Key.apiKey}&units=metric')
        try:
            response.raise_for_status()
            self.__actual = response.json()
            print("Anfrage erfolgreich")
        except requests.exceptions.HTTPError as err:
            print(f"Ein Fehler ist aufgetreten: {err}") 

    def fetchForecastData(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={self.city}&appid={Key.apiKey}&units=metric')
        try:
            response.raise_for_status()
            self.__forecast = response.json()
            print("Anfrage erfolgreich")
        except requests.exceptions.HTTPError as err:
            print(f"Ein Fehler ist aufgetreten: {err}") 

    @property
    def dataDict(self):
        if self.__actual and self.__forecast:
            print(self.__actual)
            print(self.__forecast)
        else:
            print("Geen data beschikbaar")

    @property
    def status(self):
        if self.__actual and self.__forecast:
            print(f"Actual data status: {self.__actual.get('cod', 'Onbekend')}")
            print(f"Forecast data status: {self.__forecast.get('cod', 'Onbekend')}")
        else:
            print("Geen status beschikbaar, data is niet opgehaald.")
            

    @property
    def showWeather(self):
        print(self.__actual.text)

    def dataFrame(self):
        pass

    def plotData(self):
        pass

herford = WeatherClient("herford")

herford.fetchForecastData()
herford.fetchActualData()
herford.showWeather

