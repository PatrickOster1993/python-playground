"""
Chart-View-Komponente für die grafische Darstellung der Kryptowährungsdaten.
Handhabt alle Matplotlib-basierten Visualisierungen.
"""

import matplotlib.pyplot as plt
from collections import deque
import datetime
import time

class ChartView:
    def __init__(self):
        self.timestamps = None
        self.prices = None
        self.fig = None
        self.ax = None
        self.line = None

    def setup_live_chart(self, historical_data):
        """Initialisiert das Live-Chart"""
        self.timestamps = deque(maxlen=100)
        self.prices = deque(maxlen=100)
        
        # Fülle initiale historische Daten ein
        for price_point in historical_data['prices']:
            timestamp = datetime.datetime.fromtimestamp(
                price_point[0] / 1000
            ).strftime("%H:%M:%S")
            self.timestamps.append(timestamp)
            self.prices.append(price_point[1])
        
        # Chart-Konfiguration
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(
            range(len(self.prices)), 
            self.prices, 
            label="Bitcoin Preis (USD)"
        )
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