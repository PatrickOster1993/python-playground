# # Aufgabe 2: Arbeiten mit JSON-Daten und Pandas

# **Ziel:** Eine API anfragen und die Antwortdaten mit Pandas in ein DataFrame umwandeln.

# **Aufgabe:**
# 1. Sende eine GET-Anfrage an die URL: `https://jsonplaceholder.typicode.com/users`.
# 2. Verarbeite die Antwort mit `response.json()`, um die Daten in ein Python-Dictionary zu konvertieren.
# 3. Verwende `pandas`, um die JSON-Daten in ein DataFrame umzuwandeln (nur **id**-, **name**-, **username**- und **email**-Spalten erforderlich)
# 4. Gib das DataFrames in der Konsole aus, um die Struktur der erhaltenen Daten zu überprüfen.
# ---

import requests
import pandas as pd

# Senden einer GET-Anfrage an die API
response = requests.get('https://jsonplaceholder.typicode.com/users')

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    print("STATUS_CODE: Die Anfrage war erfolgreich!")
    
    # Verarbeiten der Antwortdaten in JSON (Python-Dictionary)
    datein = response.json()
    
    # Erstellen eines DataFrames mit pandas, nur die gewünschten Spalten
    Ausgabe = pd.DataFrame(datein, columns=['id', 'name', 'username', 'email'])
    
    # DataFrame anzeigen
    print(Ausgabe)
else:
    print(f"STATUS_CODE: Anfrage fehlgeschlagen mit Statuscode {response.status_code}")
