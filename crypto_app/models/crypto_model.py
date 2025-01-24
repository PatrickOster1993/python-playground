"""
Model-Komponente für die CoinGecko API Integration.
Handhabt alle Datenoperationen und API-Zugriffe.
"""

import os
from pycoingecko import CoinGeckoAPI

class CryptoModel:
    def __init__(self):
        self.cg = self._initialize_client()
        
    def _initialize_client(self):
        """Initialisiert den CoinGecko API Client"""
        api_key = os.getenv('COINGECKO_API_KEY')
        if api_key is None:
            raise ValueError("API-Schlüssel nicht gefunden. Bitte COINGECKO_API_KEY setzen.")
        return CoinGeckoAPI()
    
    def get_current_prices(self, coin_ids, currencies):
        """Holt aktuelle Preise für angegebene Währungen"""
        return self.cg.get_price(ids=coin_ids, vs_currencies=currencies)
    
    def get_historical_data(self, coin_id, days):
        """Holt historische Preisdaten"""
        return self.cg.get_coin_market_chart_by_id(id=coin_id, vs_currency='usd', days=days)
    
    def get_categories_list(self):
        """Holt verfügbare Kategorien"""
        return self.cg.get_coins_categories_list()
    
    def get_coins_in_category(self, category_id):
        """Holt Coins einer bestimmten Kategorie"""
        return self.cg.get_coins_markets(vs_currency='usd', category=category_id)
    
    def get_exchanges_list(self):
        """Holt Liste der verfügbaren Börsen"""
        return self.cg.get_exchanges_list()
    
    def get_exchange_tickers(self, exchange_id):
        """Holt Handelsdaten einer bestimmten Börse"""
        return self.cg.get_exchanges_tickers_by_id(id=exchange_id)
    
    def get_bitcoin_price(self):
        """Holt aktuellen Bitcoin-Preis"""
        try:
            data = self.cg.get_price(ids='bitcoin', vs_currencies='usd')
            return data['bitcoin']['usd']
        except Exception as e:
            print(f"Fehler beim Abrufen des Preises: {e}")
            return None