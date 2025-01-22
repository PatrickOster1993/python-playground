import requests
import pandas as pd
import matplotlib as plt

class WeatherClient:

    def __init__(self, city):
        self.city = city
        self.__response = None

    def fetchData(self):
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid=172714e3b161108a4f5291ee357a03d2&units=metric')
        try:
            response.raise_for_status()
            self.__response = response
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

