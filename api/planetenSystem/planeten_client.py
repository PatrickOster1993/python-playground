import requests
import pandas as pd
import matplotlib.pyplot as plt

class PlanetClient:
    def __init__(self):
        self._data = None

    def fetchData(self):
        """Lädt Planeteninformationen von der API."""
        response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
        data = response.json()
        self._data = pd.DataFrame(data['bodies'])

    @property
    def dataFrame(self):
        """Gibt die Daten als DataFrame zurück."""
        return self._data

    def filterPlanets(self):
        """Filtert nur echte Planeten heraus."""
        if self._data is None:
            raise ValueError("Keine Daten vorhanden. Führe zuerst fetchData() aus.")
        return self._data[self._data['isPlanet'] == True]

    def plotPlanetRadii(self):
        """Visualisiert die Radien der Planeten als Balkendiagramm."""
        planets = self.filterPlanets()
        
        plt.figure(figsize=(10, 6))
        plt.bar(planets['name'], planets['meanRadius'])
        plt.title('Durchschnittliche Radien der Planeten')
        plt.xlabel('Planet')
        plt.ylabel('Radius in km')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# 1. Instanzen erstellen
client = PlanetClient()
client.fetchData()

# 2. Rohdaten ausgeben
print("Rohdaten:")
print(client.dataFrame.head())

# 3. Planeten filtern und anzeigen
planeten = client.filterPlanets()
print("\nGefilterte Planeten:")
print(planeten[['name', 'meanRadius']])

# 4. Radien visualisieren
client.plotPlanetRadii()