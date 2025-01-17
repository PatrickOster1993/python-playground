import requests
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from collections import deque
import os
import pandas as pd

# CoinGecko API URL für Bitcoin-Preisabfrage
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false"

# Daten initialisieren
timestamps = deque(maxlen=100)
prices = deque(maxlen=100)

# Plot initialisieren
fig, ax = plt.subplots()
line, = ax.plot([], [], label="Bitcoin Preis (USD)")
plt.title("Echtzeit Bitcoin Preis (USD)")
plt.xlabel("Zeit")
plt.ylabel("Preis (USD)")
plt.legend()

def fetch_bitcoin_price():
    """Ruft den aktuellen Bitcoin-Preis von der CoinGecko-API ab."""
    try:
        response = requests.get(COINGECKO_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(f"API Response: {data}")  # Debug-Ausgabe hinzufügen
        if 'bitcoin' in data and 'usd' in data['bitcoin']:
            return data['bitcoin']['usd']
        else:
            print("Unerwartete API-Antwortstruktur:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen des Bitcoin-Preises: {e}")
        return None

# DataFrame für Preisaufzeichnung erstellen
price_history = pd.DataFrame(columns=['Timestamp', 'Price'])

def update(frame):
    """Aktualisiert das Diagramm in Echtzeit und speichert die Daten."""
    price = fetch_bitcoin_price()
    if price is not None:
        timestamp = time.strftime("%H:%M:%S")
        timestamps.append(timestamp)
        prices.append(price)
        
        # Neue Daten zum DataFrame hinzufügen
        global price_history
        new_data = pd.DataFrame({
            'Timestamp': [timestamp],
            'Price': [price]
        })
        price_history = pd.concat([price_history, new_data], ignore_index=True)
        
        # Letzte 50 Einträge anzeigen
        print("\nLetzte Bitcoin-Preise:")
        print(price_history.tail(50))

        line.set_xdata(range(len(prices)))
        line.set_ydata(prices)

        max_ticks = 50  # Maximale Anzahl der Ticks, die angezeigt werden
        if len(timestamps) > max_ticks:
            ax.set_xticks(range(len(timestamps))[-max_ticks:])
            ax.set_xticklabels(list(timestamps)[-max_ticks:], rotation=45, ha="right")
        else:
            ax.set_xticks(range(len(timestamps)))
            ax.set_xticklabels(timestamps, rotation=45, ha="right")

        # Aktuellen Preis als Text anzeigen
        price_text.set_text(f'Aktueller Preis: ${price:,.2f}')
        
        # Diagramm aktualisieren
        ax.relim()
        ax.autoscale_view()
        
        # Y-Achse auf ±2% des aktuellen Preises begrenzen
        if price > 0:
            margin = price * 0.02
            ax.set_ylim(price - margin, price + margin)

# Text-Element für Preis-Anzeige hinzufügen
price_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12,
                    bbox=dict(facecolor='white', alpha=0.8))

# Animation starten mit 60 Sekunden Intervall
ani = FuncAnimation(fig, update, interval=15000, save_count=100, cache_frame_data=False)

# Y-Achse anpassen für bessere Sichtbarkeit von Preisänderungen
ax.set_ylim(auto=True)
ax.set_ylabel('Preis (USD)', fontsize=12)
ax.yaxis.set_major_formatter('${x:1.2f}')

# Matplotlib Backend für interaktive Anzeige setzen
plt.switch_backend('TkAgg')

# Diagramm-Einstellungen vor dem Anzeigen
plt.ion()  # Interaktiver Modus
plt.get_current_fig_manager().set_window_title('Bitcoin Preis Diagramm')

try:
    print("Abrufen der Bitcoin-Preise...")
    plt.show(block=True)
    plt.pause(0.1)  # Kurze Pause für die Aktualisierung
    print("Diagramm sollte jetzt sichtbar sein. Falls nicht, bitte prüfen:")
    print("1. Ist Tkinter installiert? (pip install python-tk)")
    print("2. Läuft das Programm in einer IDE, die Diagramme unterstützt?")
except KeyboardInterrupt:
    print("Beendet durch Benutzer.")
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
    print("Mögliche Lösungen:")
    print("- Tkinter installieren: pip install python-tk")
    print("- Anderes Backend verwenden: plt.switch_backend('Qt5Agg')")
    print("- In einer anderen Umgebung ausführen (z.B. Jupyter Notebook)")
    raise
