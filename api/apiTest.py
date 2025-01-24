import requests
import pandas as pd

class APIClient:
    def __init__(self):
        self._response = None
        self._data = None
    
    def getData(self, url):
        """Sendet GET-Request an API-Endpunkt"""
        try:
            self._response = requests.get(url, timeout=10)
            self._response.raise_for_status()
            self._data = self._response.json()
        except requests.exceptions.RequestException as e:
            print(f"API-Anfrage fehlgeschlagen: {e}")
            self._data = None
    
    def getDict(self):
        """Gibt Daten als Dictionary zurück"""
        return self._data if self._data else {}
    
    def getStatusCode(self):
        """Liefert HTTP-Statuscode der Antwort"""
        return self._response.status_code if self._response else None
    
    def showStructure(self):
        """Zeigt Rohdaten-Struktur der Antwort"""
        if self._response:
            print("=== Datenstruktur ===")
            print(self._response.text[:500] + "\n...")
        else:
            print("Keine Response-Daten vorhanden")
    
    @property
    def dataFrame(self):
        """Erzeugt Pandas DataFrame aus den Daten"""
        return pd.DataFrame(self._data) if self._data else pd.DataFrame()

if __name__ == "__main__":
    client = APIClient()
    test_url = "https://jsonplaceholder.typicode.com/posts"
    
    client.getData(test_url)
    
    print(f"\nStatuscode: {client.getStatusCode()}")
    print("\nDictionary-Auszug:")
    print({k: client.getDict()[0][k] for k in list(client.getDict()[0].keys())[:2]})
    
    client.showStructure()
    
    print("\nDataFrame-Head:")
    print(client.dataFrame.head())
