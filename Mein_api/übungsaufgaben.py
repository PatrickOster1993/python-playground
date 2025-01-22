# Aufgabe 1
import requests

# Sende GET-Anfrage
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Überprüfe Statuscode
if response.status_code == 200:
    print("Anfrage erfolgreich (Statuscode 200)")
else:
    print(f"Anfrage fehlgeschlagen (Statuscode {response.status_code})")

# Aufgabe 2
import pandas as pd

# Hole Daten von der API
response_users = requests.get("https://jsonplaceholder.typicode.com/users")
data = response_users.json()

# Erstelle DataFrame mit ausgewählten Spalten
df_users = pd.DataFrame(data, columns=["id", "name", "username", "email"])
print("\nDataFrame aus Users-API:")
print(df_users)

# Aufgabe 3
class APIClient:
    def __init__(self):
        self.response = None
    
    def getData(self, url):
        self.response = requests.get(url)
    
    def getDict(self):
        if self.response.status_code == 200:
            return self.response.json()
        else:
            print(f"Fehler bei der Anfrage. Statuscode: {self.response.status_code}")
            return None
    
    def getStatusCode(self):
        return self.response.status_code
    
    def showStructure(self):
        print("\nStruktur der Antwortdaten:")
        print(self.response.text)
    
    @property
    def dataFrame(self):
        data = self.getDict()
        if data:
            return pd.DataFrame(data)
        return pd.DataFrame()

# Verwendung der Klasse
client = APIClient()
client.getData("https://jsonplaceholder.typicode.com/posts")

print("\nStatuscode der Anfrage:", client.getStatusCode())

# Ausgabe der Dictionary-Daten
print("\nAntwort als Dictionary:")
print(client.getDict())

# Zeige Datenstruktur
client.showStructure()

# DataFrame erstellen und anzeigen
df_posts = client.dataFrame
print("\nErste 5 Einträge des DataFrames:")
print(df_posts.head())