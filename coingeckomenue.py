import os
import datetime
from pycoingecko import CoinGeckoAPI

def initialize_coingecko_client():
    api_key = os.getenv('COINGECKO_API_KEY')
    if api_key is None:
        raise ValueError("API-Schlüssel nicht gefunden. Bitte stellen Sie sicher, dass die Umgebungsvariable 'COINGECKO_API_KEY' gesetzt ist.")
    return CoinGeckoAPI()

def get_current_prices(cg):
    coins = input("Geben Sie die IDs der Kryptowährungen ein (durch Kommas getrennt, z.B. bitcoin,ethereum): ")
    vs_currencies = input("Geben Sie die Vergleichswährungen ein (durch Kommas getrennt, z.B. usd,eur): ")
    prices = cg.get_price(ids=coins.split(','), vs_currencies=vs_currencies.split(','))
    print("Aktuelle Preise:")
    for coin, data in prices.items():
        for currency, price in data.items():
            print(f"{coin} in {currency}: {price}")

def get_historical_data(cg):
    coin_id = input("Geben Sie die ID der Kryptowährung ein (z.B. bitcoin): ")
    days = input("Geben Sie die Anzahl der Tage für die historischen Daten ein (z.B. 30): ")
    data = cg.get_coin_market_chart_by_id(id=coin_id, vs_currency='usd', days=days)
    print(f"Historische Preisdaten für {coin_id} in den letzten {days} Tagen:")
    for price_point in data['prices']:
        timestamp = datetime.datetime.fromtimestamp(price_point[0] / 1000)
        price = price_point[1]
        print(f"Datum: {timestamp}, Preis: {price} USD")

def compare_coins_in_category(cg):
    categories = cg.get_coins_categories_list()
    print("Verfügbare Kategorien:")
    for category in categories:
        print(f"- {category['name']} (ID: {category['id']})")
    category_id = input("Geben Sie die ID der gewünschten Kategorie ein: ")
    coins = cg.get_coins_markets(vs_currency='usd', category=category_id)
    print(f"Coins in der Kategorie '{category_id}':")
    for coin in coins:
        print(f"Name: {coin['name']}, Symbol: {coin['symbol']}, Preis: {coin['current_price']} USD, Marktkapitalisierung: {coin['market_cap']} USD")

def analyze_exchange_data(cg):
    exchanges = cg.get_exchanges_list()
    print("Verfügbare Börsen:")
    for exchange in exchanges:
        print(f"- {exchange['name']} (ID: {exchange['id']})")
    exchange_id = input("Geben Sie die ID der gewünschten Börse ein: ")
    tickers = cg.get_exchanges_tickers_by_id(id=exchange_id)
    print(f"Handelspaare an der Börse '{exchange_id}':")
    for ticker in tickers['tickers']:
        print(f"Handelspaar: {ticker['base']}/{ticker['target']}, Volumen: {ticker['volume']}")

def monitor_derivatives(cg):
    derivatives_exchanges = cg.get_derivatives_exchanges()
    print("Verfügbare Derivate-Börsen:")
    for exchange in derivatives_exchanges:
        print(f"- {exchange['name']} (ID: {exchange['id']})")
    exchange_id = input("Geben Sie die ID der gewünschten Derivate-Börse ein: ")
    derivatives = cg.get_derivatives_exchanges_by_id(id=exchange_id)
    print(f"Derivate an der Börse '{exchange_id}':")
    for derivative in derivatives['tickers']:
        print(f"Symbol: {derivative['symbol']}, Basiswert: {derivative['base']}, Zielwert: {derivative['target']}, Open Interest: {derivative['open_interest_usd']} USD")

def main_menu():
    cg = initialize_coingecko_client()
    while True:
        print("\nCoinGecko API Abfrage Menü:")
        print("1. Aktuelle Preisinformationen abrufen")
        print("2. Historische Preisentwicklungen untersuchen")
        print("3. Vergleich von Coins innerhalb einer Kategorie")
        print("4. Analyse von Börsenhandelsdaten")
        print("5. Überwachung von Derivatemärkten")
        print("6. Beenden")
        choice = input("Bitte wählen Sie eine Option (1-6): ")

        if choice == '1':
            get_current_prices(cg)
        elif choice == '2':
            get_historical_data(cg)
        elif choice == '3':
            compare_coins_in_category(cg)
        elif choice == '4':
            analyze_exchange_data(cg)
        elif choice == '5':
            monitor_derivatives(cg)
        elif choice == '6':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte versuchen Sie es erneut.")
            return

main_menu()
