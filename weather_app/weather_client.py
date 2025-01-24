import requests
from exceptions import InvalidCityError, APIError
import pandas as pd  
import matplotlib.pyplot as plt  
from io import BytesIO  
import base64  

class WeatherClient:  
    def __init__(self):  
        self.base_url = "https://api.open-meteo.com/v1/forecast"  
        self._data = None  

    def fetch_data(self, city: str) -> None:  
        coords = self._get_coordinates(city)  
        params = {  
            'latitude': coords[0],  
            'longitude': coords[1],  
            'daily': 'temperature_2m_max',  
            'timezone': 'auto'  
        }  
        
        response = requests.get(self.base_url, params=params)  
        response.raise_for_status()  
        self._data = response.json()  

    def generate_plot(self) -> str:  
        df = pd.DataFrame({  
            'date': self._data['daily']['time'],  
            'temp': self._data['daily']['temperature_2m_max']  
        })  
        
        plt.figure(figsize=(10,6))  
        plt.plot(df['date'], df['temp'], marker='o', linestyle='--')  
        plt.title('Temperaturverlauf')  
        plt.xlabel('Datum')  
        plt.ylabel('Temperatur (°C)')  
        plt.xticks(rotation=45)  
        plt.tight_layout()  
        
        buffer = BytesIO()  
        plt.savefig(buffer, format='png')  
        plt.close()  
        return base64.b64encode(buffer.getvalue()).decode('utf-8')  

    def _get_coordinates(self, city: str) -> tuple:
        try:
            response = requests.get(
                "https://nominatim.openstreetmap.org/search",
                params={
                    'q': city,
                    'format': 'json',
                    'limit': 1
                },
                headers={'User-Agent': 'WeatherApp/1.0'}
            )
            response.raise_for_status()
            
            data = response.json()
            if not data:
                raise InvalidCityError(f"Stadt '{city}' nicht gefunden")
                
            return (float(data[0]['lat']), float(data[0]['lon']))
            
        except requests.RequestException as e:
            raise APIError(f"Koordinaten-Service fehlgeschlagen: {str(e)}") from e

    @property  
    def data_dict(self):  
        return self._data