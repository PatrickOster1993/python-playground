import os
import datetime
from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time

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

def show_live_price_chart(cg):
    # Daten initialisieren
    timestamps = deque(maxlen=100)
    prices = deque(maxlen=100)
    
    # Diagramm initialisieren
    fig, ax = plt.subplots()
    line, = ax.plot([], [], label="Bitcoin Preis (USD)")
    plt.title("Echtzeit Bitcoin Preis (USD)")
    plt.xlabel("Zeit")
    plt.ylabel("Preis (USD)")
    plt.legend()
    
    def fetch_bitcoin_price():
        try:
            data = cg.get_price(ids='bitcoin', vs_currencies='usd')
            return data['bitcoin']['usd']
        except Exception as e:
            print(f"Fehler beim Abrufen des Preises: {e}")
            return None
    
    def update(frame):
        price = fetch_bitcoin_price()
        if price is not None:
            timestamp = time.strftime("%H:%M:%S")
            timestamps.append(timestamp)
            prices.append(price)
            
            line.set_xdata(range(len(prices)))
            line.set_ydata(prices)
            
            ax.set_xticks(range(len(timestamps)))
            ax.set_xticklabels(timestamps, rotation=45, ha="right")
            
            ax.relim()
            ax.autoscale_view()
            plt.pause(0.1)
    
    print("Live Bitcoin-Preisdiagramm wird gestartet...")
    ani = FuncAnimation(fig, update, interval=15000)
    plt.show()

def main_menu():
    cg = initialize_coingecko_client()
    while True:
        print("\n--- CoinGecko Menü ---")
        print("1. Aktuelle Preisinformationen abrufen")
        print("2. Historische Preisentwicklungen untersuchen")
        print("3. Vergleich von Coins innerhalb einer Kategorie")
        print("4. Analyse von Börsenhandelsdaten")
        print("5. Überwachung von Derivatemärkten")
        print("6. Live Bitcoin-Preisdiagramm")
        print("7. Beenden")
        choice = input("Bitte wählen Sie eine Option (1-7): ")

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
            show_live_price_chart(cg)
        elif choice == '7':
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main_menu()
