import requests
import pandas as pd
import matplotlib.pyplot as plt

class PlanetClient:

    def __init__(self,url_ein):
        try:
            self.__url = url_ein
            self.__data = {}
            self._filterPlanets 
        except Exception as e:
            print("Fehler", {e})


    
def fetchData(self):
    response = requests.get(self._url)
    code = response.status_code
    if response.status_code == 200:
        self._data = response.json()
    else:
        print(f"Request failed with code {code}!")



 
def filterPlanets(self):
    pass

def plotPlanetRadii(self):
    pass

@property
def dataFrame(self):
    try:
        return pd.DataFrame(self._data)
    except:
        return pd.DataFrame(self._data)
   




    
    # url = "https://api.le-systeme-solaire.net/rest/bodies/"