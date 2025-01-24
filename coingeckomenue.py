"""
Ein interaktives Menüprogramm zur Abfrage und Visualisierung von Kryptowährungsdaten über die CoinGecko API.
Implementiert nach dem MVC (Model-View-Controller) Pattern.
"""

import os
import datetime
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time

# Model: Handhabt Datenlogik und API-Kommunikation
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

# View: Handhabt die Darstellung und Benutzerinteraktion
class CryptoView:
    def show_menu(self):
        """Zeigt das Hauptmenü an"""
        print("\n--- CoinGecko Menü ---")
        print("1. Aktuelle Preisinformationen abrufen")
        print("2. Historische Preisentwicklungen untersuchen")
        print("3. Vergleich von Coins innerhalb einer Kategorie")
        print("4. Analyse von Börsenhandelsdaten")
        print("5. Live Bitcoin-Preisdiagramm")
        print("6. Beenden")
    
    def get_user_input(self, prompt):
        """Holt Benutzereingabe"""
        return input(prompt)
    
    def show_prices(self, prices):
        """Zeigt aktuelle Preise an"""
        print("Aktuelle Preise:")
        for coin, data in prices.items():
            for currency, price in data.items():
                print(f"{coin} in {currency}: {price}")
    
    def show_historical_data(self, data, coin_id, days):
        """Zeigt historische Daten an"""
        print(f"Historische Preisdaten für {coin_id} in den letzten {days} Tagen:")
        for price_point in data['prices']:
            timestamp = datetime.datetime.fromtimestamp(price_point[0] / 1000)
            price = price_point[1]
            print(f"Datum: {timestamp}, Preis: {price} USD")
    
    def show_categories(self, categories):
        """Zeigt verfügbare Kategorien an"""
        print("Verfügbare Kategorien:")
        for category in categories:
            print(f"- {category.get('name', 'Unbekannte Kategorie')} (ID: {category.get('category_id', 'n/a')})")
    
    def show_category_coins(self, coins, category_id):
        """Zeigt Coins einer Kategorie an"""
        print(f"Coins in der Kategorie '{category_id}':")
        for coin in coins:
            print(f"Name: {coin['name']}, Symbol: {coin['symbol']}, "
                f"Preis: {coin['current_price']} USD, "
                f"Marktkapitalisierung: {coin['market_cap']} USD")
    
    def show_exchanges(self, exchanges):
        """Zeigt verfügbare Börsen an"""
        print("Verfügbare Börsen:")
        for exchange in exchanges:
            print(f"- {exchange['name']} (ID: {exchange['id']})")
    
    def show_exchange_data(self, tickers, exchange_id):
        """Zeigt Börsendaten an"""
        print(f"Handelspaare an der Börse '{exchange_id}':")
        for ticker in tickers['tickers']:
            print(f"Handelspaar: {ticker['base']}/{ticker['target']}, "
                f"Volumen: {ticker['volume']}")

class ChartView:
    def setup_live_chart(self, historical_data):
        """Initialisiert das Live-Chart"""
        self.timestamps = deque(maxlen=100)
        self.prices = deque(maxlen=100)
        
        # Fülle initiale historische Daten ein
        for price_point in historical_data['prices']:
            timestamp = datetime.datetime.fromtimestamp(price_point[0] / 1000).strftime("%H:%M:%S")
            self.timestamps.append(timestamp)
            self.prices.append(price_point[1])
        
        # Chart-Konfiguration
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(range(len(self.prices)), self.prices, label="Bitcoin Preis (USD)")
        plt.title("Bitcoin Preis der letzten Stunde (USD)")
        plt.xlabel("Zeit")
        plt.ylabel("Preis (USD)")
        plt.legend()
        
        return self.fig, self.ax, self.line
    
    def update_chart(self, frame, price):
        """Aktualisiert das Chart mit neuen Daten"""
        if price is not None:
            timestamp = time.strftime("%H:%M:%S")
            self.timestamps.append(timestamp)
            self.prices.append(price)
            
            self.line.set_xdata(range(len(self.prices)))
            self.line.set_ydata(self.prices)
            
            self.ax.set_xticks(range(len(self.timestamps)))
            self.ax.set_xticklabels(self.timestamps, rotation=45, ha="right")
            
            self.ax.relim()
            self.ax.autoscale_view()
            plt.pause(0.1)

# Controller: Steuert den Programmablauf und verbindet Model und View
class CryptoController:
    def __init__(self):
        self.model = CryptoModel()
        self.view = CryptoView()
        self.chart_view = ChartView()
    
    def run(self):
        """Hauptprogrammschleife"""
        while True:
            self.view.show_menu()
            choice = self.view.get_user_input("Bitte wählen Sie eine Option (1-6): ")
            
            if choice == '1':
                self.handle_current_prices()
            elif choice == '2':
                self.handle_historical_data()
            elif choice == '3':
                self.handle_category_comparison()
            elif choice == '4':
                self.handle_exchange_analysis()
            elif choice == '5':
                self.handle_live_chart()
            elif choice == '6':
                print("Programm wird beendet.")
                break
            else:
                print("Ungültige Auswahl, bitte versuchen Sie es erneut.")
    
    def handle_current_prices(self):
        """Verarbeitet Preisabfragen"""
        coins = self.view.get_user_input("Geben Sie die IDs der Kryptowährungen ein (durch Kommas getrennt): ")
        currencies = self.view.get_user_input("Geben Sie die Vergleichswährungen ein (durch Kommas getrennt): ")
        prices = self.model.get_current_prices(coins.split(','), currencies.split(','))
        self.view.show_prices(prices)
    
    def handle_historical_data(self):
        """Verarbeitet historische Datenabfragen"""
        coin_id = self.view.get_user_input("Geben Sie die ID der Kryptowährung ein: ")
        days = self.view.get_user_input("Geben Sie die Anzahl der Tage ein: ")
        data = self.model.get_historical_data(coin_id, days)
        self.view.show_historical_data(data, coin_id, days)
    
    def handle_category_comparison(self):
        """Verarbeitet Kategorienvergleiche"""
        try:
            categories = self.model.get_categories_list()
            self.view.show_categories(categories)
            category_id = self.view.get_user_input("Geben Sie die ID der gewünschten Kategorie ein: ")
            coins = self.model.get_coins_in_category(category_id)
            self.view.show_category_coins(coins, category_id)
        except Exception as e:
            print(f"Fehler beim Kategorievergleich: {str(e)}")
    
    def handle_exchange_analysis(self):
        """Verarbeitet Börsenanalysen"""
        exchanges = self.model.get_exchanges_list()
        self.view.show_exchanges(exchanges)
        exchange_id = self.view.get_user_input("Geben Sie die ID der gewünschten Börse ein: ")
        tickers = self.model.get_exchange_tickers(exchange_id)
        self.view.show_exchange_data(tickers, exchange_id)
    
    def handle_live_chart(self):
        """Verarbeitet Live-Chart-Anzeige"""
        historical_data = self.model.get_historical_data('bitcoin', 0.042)
        fig, ax, line = self.chart_view.setup_live_chart(historical_data)
        
        def update(frame):
            price = self.model.get_bitcoin_price()
            self.chart_view.update_chart(frame, price)
        
        print("Live Bitcoin-Preisdiagramm wird gestartet...")
        ani = FuncAnimation(fig, update, interval=15000)
        plt.show()

if __name__ == "__main__":
    controller = CryptoController()
    controller.run()
