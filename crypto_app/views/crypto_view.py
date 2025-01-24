"""
View-Komponente für die Benutzerinteraktion und Textausgabe.
Handhabt alle Menü- und Datenanzeigen.
"""

import datetime

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
            print(f"- {category.get('name', 'Unbekannte Kategorie')} "
                  f"(ID: {category.get('category_id', 'n/a')})")
    
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