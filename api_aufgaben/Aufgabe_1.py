# Hier testen wir die in "api.md" vermittelten Inhalte aus!
import requests

# Senden einer GET-Anfrage an die API
response = requests.get('https://jsonplaceholder.typicode.com/users')


# **Ziel:** Deine erste Anfrage an eine API senden und den Statuscode der Antwort auswerten.

# **Aufgabe:**
# 1. Sende eine GET-Anfrage an die URL: `https://jsonplaceholder.typicode.com/posts/1`.
# 2. Überprüfe den Statuscode der Antwort und gib eine Nachricht aus, die anzeigt, ob die Anfrage erfolgreich war oder nicht (Nutze `response.status_code`).

# **Hinweis:** Eine erfolgreiche Antwort hat den Statuscode **200**.

# Überprüfen des Statuscodes der Antwort
if response.status_code == 200:
    # Verarbeiten der Antwort, falls erfolgreich
    print("STATUS_CODE: Die Anfrage war erfolgreich!")
    #print(response.json()) # bessere Weiterverarbeitung (Python dict)
    print(response.text) # bessere Lesbarkeit (für Konsole)
    # print(response.content) # für Verarbeitung von nicht-textellen Daten / Binärdaten (z. B. Bilder / Audios)
else: 
    print(f"Derfehlercode lautet : {response.status_code}")
# # Alternatives Abfangen von Fehlern / gescheiterten Anfragen
# # für mich persönlich präferierte Variante, da über echtes Exception-Handling!
# try:
#     response.raise_for_status()
#     print("RAISE_FOR_STATUS: Die Anfrage war erfolgreich!")
# except requests.exceptions.HTTPError as err:
#     print(f"Ein Fehler ist aufgetreten: {err}")