import matplotlib.pyplot as plt
import requests
import pandas as pd

class WeatherClient:

    def __init__(self, url_ein):
        self.__url = url_ein
        self.__response = None
    
    def fetchData(self):
        self.__response = requests.get(self.__url)

    def showWeather(self):
        if self.status == 200:
            print(self.__response.text)
        else:
            print("Anfrage an Server nicht erfolgreich!")

    @property
    def dataDict(self):
        if self.status == 200:
            return self.__response.json()["daily"]
        else:
            return {}
    
    @property
    def dataFrame(self):
        return pd.DataFrame(self.dataDict)

    @property
    def status(self):
        return self.__response.status_code
    
client = WeatherClient(url_ein="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max&timezone=auto")
client.fetchData()
print("Antwort im dict-Format:", client.dataDict)
print("Status Code:", client.status)
print("####################################################")
client.showWeather()
print("####################################################")
df = client.dataFrame
print(df.head())

# Plotten
plt.style.use('dark_background')
plt.figure(figsize=(10, 5))
plt.plot(df["time"], df["temperature_2m_max"], label='Temperatur', color='#F9C0AB')

# Achsenbeschriftung
plt.xlabel("Tag")
plt.ylabel("Temperatur (°C)")
plt.title("Maximale Temperaturen in Berlin")
plt.legend()

# Gitternetz hinzufügen
plt.grid(axis='y', linewidth=0.5, alpha=0.25)

# Diagramm anzeigen
plt.show()