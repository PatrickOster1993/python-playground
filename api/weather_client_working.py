import requests
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Optional

class WeatherClient:
    """Klasse zur Abfrage und Visualisierung von Wetterdaten der Open-Meteo-API
    
    Attributes:
        base_url (str): Basis-URL der API
        _data (Optional[Dict]): Rohdaten der API-Antwort
        _response (Optional[requests.Response]): HTTP-Response-Objekt
    """
    
    def __init__(self, base_url: str = "https://api.open-meteo.com/v1/forecast"):
        """Initialisiert den WeatherClient mit der API-URL
        
        Args:
            base_url (str, optional): Basis-URL der API. Defaults zur Open-Meteo-API.
        """
        self.base_url = base_url
        self._data: Optional[Dict] = None
        self._response: Optional[requests.Response] = None
    
    def fetch_data(self, city: str) -> None:
        """Holt Wetterdaten für eine spezifische Stadt
        
        Args:
            city (str): Stadtname für die Wetterabfrage
            
        Raises:
            ValueError: Bei ungültiger Stadtangabe
            ConnectionError: Bei API-Verbindungsproblemen
        """
        try:
            # TODO: Koordinatenabfrage für Stadtnamen implementieren
            params = {
                'latitude': 52.52,  # Beispielwert für Berlin
                'longitude': 13.41,
                'daily': 'temperature_2m_max',
                'timezone': 'auto'
            }
            
            self._response = requests.get(self.base_url, params=params, timeout=10)
            self._response.raise_for_status()
            self._data = self._response.json()
            
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"API-Fehler: {str(e)}") from e
    
    @property
    def data_dict(self) -> Dict:
        """Liefert die Rohdaten als Dictionary
        
        Returns:
            Dict: Wetterdaten im Dictionary-Format
            
        Raises:
            RuntimeError: Wenn keine Daten vorhanden sind
        """
        if self._data is None:
            raise RuntimeError("Keine Daten vorhanden. Führen Sie erst fetch_data() aus.")
        return self._data
    
    @property
    def status(self) -> int:
        """HTTP-Statuscode der letzten Anfrage
        
        Returns:
            int: Statuscode (200 bei Erfolg)
        """
        return self._response.status_code if self._response else 0
    
    def show_weather(self) -> None:
        """Zeigt die Temperaturdaten formatiert in der Konsole an"""
        if not self._data:
            print("Keine Wetterdaten verfügbar")
            return
            
        temps = self._data['daily']['temperature_2m_max']
        dates = self._data['daily']['time']
        
        print(f"\n{'Datum':<15} | {'Max. Temperatur (°C)':<18}")
        print('-'*34)
        for date, temp in zip(dates, temps):
            print(f"{date:<15} | {temp:^18.1f}")
    
    @property
    def data_frame(self) -> pd.DataFrame:
        """Erstellt einen DataFrame aus den Wetterdaten
        
        Returns:
            pd.DataFrame: DataFrame mit Datum und Temperaturen
        """
        return pd.DataFrame({
            'date': self._data['daily']['time'],
            'temperature_2m_max': self._data['daily']['temperature_2m_max']
        })
    
    def plot_weather(self) -> plt.Figure:
        """Erstellt ein Liniendiagramm der Temperaturdaten
        
        Returns:
            plt.Figure: Matplotlib Figure-Objekt
        """
        df = self.data_frame
        fig = plt.figure(figsize=(10, 6))
        plt.plot(df['date'], df['temperature_2m_max'], marker='o', linestyle='--')
        
        plt.title("Maximale Tagestemperaturen")
        plt.xlabel("Datum")
        plt.ylabel("Temperatur (°C)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        
        return fig

# Beispielverwendung
if __name__ == "__main__":
    client = WeatherClient()
    try:
        client.fetch_data("Berlin")
        print(f"API-Statuscode: {client.status}")
        print("\nDatenauszug:")
        print(client.data_dict['daily'].keys())
        
        client.show_weather()
        
        df = client.data_frame
        print("\nDataFrame-Beispiel:")
        print(df.head())
        
        fig = client.plot_weather()
        plt.show()
        
    except Exception as e:
        print(f"Fehler: {str(e)}")