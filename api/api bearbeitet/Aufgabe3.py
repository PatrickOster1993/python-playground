import requests
import pandas as pd

## Aufgabe 3: Erstellen einer kleinen Klasse für API-Daten (OOP)

# **Ziel:** Eine Klasse erstellen, die Daten von einer API abruft und in einer benutzerfreundlichen Art und Weise darstellt. Die Antwort wird als Pandas DataFrame gespeichert.

# **Aufgabe:**
# 1. Erstelle eine Klasse `APIClient`, die folgende Attribute/Methoden hat:
#    - **`getData(url)`**: Sendet eine GET-Anfrage an die übergebene URL und speichert die Antwort (= response)
#    - **`getDict()`**: Gibt die Antwort im **Dictionary-Format** zurück, falls die Anfrage erfolgreich war.
#    - **`getStatusCode()`**: Gibt den Statuscode der Antwort zurück.
#    - **`showStructure()`**: Gibt die Struktur der Antwort im **Textformat** aus, damit du sehen kannst, wie der Aufbau der Daten strukturiert ist (Tipp: response.text).
#    - **`dataFrame`**: Gibt die Antwortdaten als **Pandas DataFrame** zurück (Tipp: property verwenden).
# 2. Erstelle eine Instanz der Klasse und rufe die Methoden mit der URL `https://jsonplaceholder.typicode.com/posts` auf, um die Daten und den Statuscode zu erhalten.
# 3. Gib die Antwort im **Dictionary-Format** aus und zeige den Statuscode der Anfrage.
# 4. Nutze die Methode `showStructure()`, um die Struktur der Daten in der Konsole darzustellen.
# 5. Speichere die Antwort als Pandas DataFrame und gib die ersten 5 Zeilen des DataFrames aus.

# >**Hinweis:** Achte darauf, Fehler zu behandeln, falls die Anfrage fehlschlägt (z.B. durch den Statuscode 404 oder 500).
# ---

# Aufgabe 3

class APIClient:
    def __init__(self, ):
        self.response = None
    
    def getData(self, url):
        self.response = requests.get(url)
        return self.response
        
    def getDict(self):
        return self.response.json()
    
    def getStatusCode(self):
        return self.response.status_code
    
    def showStructure(self):
        return self.response.text
    
    def printDataFrame(self, head=5):
        if self.response:
            df = pd.DataFrame(self.response.json())
            return df.head(head)  # Return only the first 5 rows
        return None

client = APIClient()
client.getData("https://jsonplaceholder.typicode.com/posts")
print(client.response)
#print(client.getDict())
#print(client.showStructure())
#print(client.printDataFrame())

