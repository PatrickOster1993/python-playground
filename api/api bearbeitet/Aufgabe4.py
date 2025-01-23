# ## Aufgabenbeschreibung

# Erstelle eine Klasse `WeatherClient`, die folgende Attribute und Methoden besitzt:

# ### Attribute/Methoden

# 1. **`fetchData(city)`**
#    - Sendet eine Anfrage an die Wetter-API mit dem übergebenen Stadtnamen.
#    - Die Daten werden in einem internen Attribut gespeichert.
#    - *Nutze z. B. die API:*
#      ```
#      https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max&timezone=auto
#      ```
#      *(für Berlin)*

# 2. **`dataDict`** (Property)
#    - Gibt die Antwortdaten im Dictionary-Format zurück.

# 3. **`status`** (Property)
#    - Gibt den HTTP-Statuscode der Anfrage zurück.

# 4. **`showWeather()`**
#    - Gibt die Temperaturdaten (z. B. die maximalen Tagestemperaturen der nächsten Woche) im Konsolenformat aus.

# 5. **`dataFrame`** (Property)
#    - Gibt die Daten als Pandas DataFrame zurück.

# 6. **`plotWeather()`**
#    - Visualisiert die Temperaturdaten als Liniendiagramm (z. B. Temperatur über die Zeit mit Matplotlib).

import requests
import pandas as pd
import matplotlib.pyplot as plt

class WeatherClient:
    def __init__(self):
        self.response = None
        self.api_key = "c08779c22c344c99b1bfbd16f7f3a4d9"
        self.latitude = None
        self.longitude = None
    
    def fetchData(self, city):
        self.latitude, self.longitude = self._get_coordinates(city)
        self.response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&daily=temperature_2m_max&timezone=auto")
        return self.response
    
    def _get_coordinates(self, city):
        geocode_url = f"https://api.opencagedata.com/geocode/v1/json?q={city}&key={self.api_key}"
        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()
        if geocode_data['results']:
            self.latitude = geocode_data['results'][0]['geometry']['lat']
            self.longitude = geocode_data['results'][0]['geometry']['lng']
            return self.latitude, self.longitude
        else:
            raise ValueError("City not found")
    
    @property
    def dataDict(self):
        return self.response.json()
    
    @property
    def status(self):
        return self.response.status_code

    def showWeather(self):
        if self.response:
            daily_data = self.response.json()['daily']
            for date, temp in zip(daily_data['time'], daily_data['temperature_2m_max']):
                print(f"Date: {date}, Max Temperature: {temp}°C")
    
    
    @property
    def dataFrame(self):
        if self.response:
            return pd.DataFrame(self.response.json())
        return None
    
    def plotWeather(self):
        if self.response:
            daily_data = self.response.json()['daily']
            dates = daily_data['time']
            temperatures = daily_data['temperature_2m_max']
            plt.plot(dates, temperatures)
            plt.xlabel("Date")
            plt.ylabel("Max Temperature (°C)")
            plt.title("Max Temperatures over Time")
            plt.show()
        else:
            print("No data available for plotting")
    
client = WeatherClient()

client.fetchData("Köln")
#print(client.status)
#print(client.fetchData().text)
client.showWeather()
#print(client.dataFrame)
client.plotWeather()