# ## Aufgabe 1: Senden einer einfachen GET-Anfrage

# **Ziel:** Deine erste Anfrage an eine API senden und den Statuscode der Antwort auswerten.

# **Aufgabe:**
# 1. Sende eine GET-Anfrage an die URL: `https://jsonplaceholder.typicode.com/posts/1`.
# 2. Überprüfe den Statuscode der Antwort und gib eine Nachricht aus, die anzeigt, ob die Anfrage erfolgreich war oder nicht (Nutze `response.status_code`).

# **Hinweis:** Eine erfolgreiche Antwort hat den Statuscode **200**.

# ---

import requests

# Aufgabe 1
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    print("Anfrage erfolgreich")
else:
    print("Anfrage fehlgeschlagen")