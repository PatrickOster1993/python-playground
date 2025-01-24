import pandas as pd
import requests

class PlanetClient:
    def __init__(self, url):
        self.__url = url
        self.__response = None
        self.__filteredPlanets = None

    def fetchData(self):
        self.__response = requests.get(self.__url)
    
    @property
    def status(self):
        return self.__response.status_code
    
    @property
    def showWeather(self):
        if self.status == 200:
            print(self.__response.text)
        else:
            print("Anfrage an Server nicht erfolgreich!")

    @property
    def dataFrame(self):
        return pd.DataFrame(self.__response.json()["bodies"])
    
    @property
    def filterPlanets(self):
        filter_condition = self.dataFrame["isPlanet"] == True
        self.__filteredPlanets = self.dataFrame[filter_condition]
        return self.__filteredPlanets

client = PlanetClient("https://api.le-systeme-solaire.net/rest/bodies/")
client.fetchData()
print(client.filterPlanets)