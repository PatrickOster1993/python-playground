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
        print("1. Aktuelle Preise anzeigen")
        print("2. Historische Daten anzeigen")
        print("3. Live Bitcoin-Preisdiagramm")
        print("4. Beenden")
        choice = input("Auswahl: ")
        
        if choice == "1":
            get_current_prices(cg)
        elif choice == "2":
            get_historical_data(cg)
        elif choice == "3":
            show_live_price_chart(cg)
        elif choice == "4":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Auswahl, bitte erneut versuchen.")

if __name__ == "__main__":
    main_menu()
