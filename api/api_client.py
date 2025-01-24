import pandas as pd
import requests
import argparse
import logging
from typing import Optional, Dict, Any, List
from pandas import json_normalize

# Logger konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor:
    """Verarbeitet komplexe JSON-Strukturen für DataFrame-Konvertierung"""
    
    @staticmethod
    def flatten_data(data: Dict, max_depth: int = 2) -> Dict:
        """
        Transformiert verschachtelte Strukturen in flache Schlüssel
        
        Args:
            data (dict): Rohdaten von der API
            max_depth (int): Maximale Verschachtelungstiefe
            
        Returns:
            dict: Transformierte Datenstruktur
        """
        try:
            return json_normalize(data, max_level=max_depth, sep='_').to_dict(orient='records')[0]
        except Exception as e:
            logger.error(f"Flattening Error: {str(e)}")
            return {}

class APIClient:
    """Erweiterter API-Client mit Data-Processing-Funktionen"""
    
    def __init__(self, timeout: int = 10, verify_ssl: bool = True):
        self.session = requests.Session()
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.processor = DataProcessor()

    def fetch_data(self, url: str, params: Optional[Dict] = None) -> Optional[Dict]:
        """Holt und verarbeitet API-Daten"""
        try:
            response = self.session.get(
                url, 
                params=params, 
                timeout=self.timeout,
                verify=self.verify_ssl
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"API Request Failed: {str(e)}")
            return None

def create_dataframe(data: Dict) -> Optional[pd.DataFrame]:
    """Erstellt DataFrame mit automatischer Strukturanalyse"""
    try:
        flat_data = DataProcessor.flatten_data(data)
        df = pd.DataFrame([flat_data])
        
        # Handle komplexe Datentypen
        df = df.map(lambda x: str(x) if isinstance(x, (list, dict)) else x)
        
        return df.replace({pd.NaT: None}).dropna(axis=1, how='all')
    except Exception as e:
        logger.error(f"DataFrame Creation Error: {str(e)}")
        return None

def debug_data_structure(data: Dict) -> None:
    """Analysiert die Datenstruktur"""
    print("\n=== Datenstruktur-Debug ===")
    print(f"Top-Level Keys: {list(data.keys())}")
    for key, value in data.items():
        if isinstance(value, list):
            print(f"📂 {key}: Liste ({len(value)} Elemente)")
            if value and isinstance(value[0], dict):
                print(f"   🔑 Unterkeys: {list(value[0].keys())}")
        elif isinstance(value, dict):
            print(f"📁 {key}: Dictionary ({len(value)} Einträge)")

def interactive_column_selection(df: pd.DataFrame) -> None:
    """Interaktive Spaltenauswahl mit erweiterten Optionen"""
    print("\nVerfügbare Spalten:")
    for idx, col in enumerate(df.columns, 1):
        print(f"{idx:2}. {col}")
        
    while True:
        try:
            selection = input("\nSpaltennummern (kommagetrennt): ")
            cols = [int(s.strip()) - 1 for s in selection.split(',')]
            valid = all(0 <= c < len(df.columns) for c in cols)
            
            if valid:
                selected_cols = [df.columns[c] for c in cols]
                print(f"\nAuswahl: {', '.join(selected_cols)}")
                print(df[selected_cols].head())
                break
            print("⚠️ Ungültige Auswahl - bitte Nummern erneut eingeben")
        except ValueError:
            print("❌ Ungültiges Format - nur Zahlen und Kommas erlaubt")

def main():
    """Hauptfunktion mit erweiterten Optionen"""
    parser = argparse.ArgumentParser(description='API Client mit DataFrame-Unterstützung')
    parser.add_argument('--url', required=True, help='API Endpoint URL')
    parser.add_argument('--debug', action='store_true', help='Debug-Modus aktivieren')
    args = parser.parse_args()
    
    client = APIClient()
    data = client.fetch_data(args.url)
    
    if data and args.debug:
        debug_data_structure(data)
    
    if data:
        df = create_dataframe(data)
        if df is not None and not df.empty:
            interactive_column_selection(df)
        else:
            logger.error("DataFrame konnte nicht erstellt werden")

if __name__ == "__main__":
    main()