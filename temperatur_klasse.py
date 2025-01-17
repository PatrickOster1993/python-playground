import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TemperaturAnalyse:
    def __init__(self, historische_daten, aktuelle_woche):
        """
        Initialisiert die TemperaturAnalyse-Klasse mit historischen Daten und aktuellen Wochendaten
        
        Args:
            historische_daten (np.array): 2D-Array mit historischen Temperaturdaten (Wochen x Tage)
            aktuelle_woche (np.array): Array mit Temperaturen der aktuellen Woche
        """
        self.historische_daten = historische_daten
        self.aktuelle_woche = aktuelle_woche
        self.wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        self.durchschnittstemperaturen = None
        self.max_temp = None
        self.min_temp = None
        self.dataframe = None
        
    def berechne_statistiken(self):
        """Berechnet Durchschnitt, Maximum und Minimum der Temperaturen"""
        self.durchschnittstemperaturen = np.mean(self.historische_daten, axis=0)
        self.max_temp = np.max(self.durchschnittstemperaturen)
        self.min_temp = np.min(self.durchschnittstemperaturen)
        
    def erstelle_dataframe(self):
        """Erstellt ein Pandas DataFrame mit den berechneten Daten"""
        self.dataframe = pd.DataFrame({
            "Tag": self.wochentage,
            "Durchschnittstemperatur (°C)": self.durchschnittstemperaturen
        })
        
    def plot_daten(self):
        """Erstellt ein Liniendiagramm der Temperaturdaten"""
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        
        # Plot Durchschnittstemperaturen
        plt.plot(self.dataframe["Tag"], 
                self.dataframe["Durchschnittstemperatur (°C)"], 
                label='Durchschnittstemperatur', 
                color='#ABE4F9')
        
        # Plot aktuelle Woche
        plt.plot(self.dataframe["Tag"], 
                self.aktuelle_woche, 
                label='Aktuelle Woche', 
                color='#F9E7AB')
        
        # Horizontale Linien für Max und Min
        plt.axhline(y=self.max_temp, color='#ABF9E7', linestyle=':', label='Max. Temperatur')
        plt.axhline(y=self.min_temp, color='#F9ABBD', linestyle=':', label='Min. Temperatur')
        
        # Achsenbeschriftungen und Titel
        plt.xlabel("Wochentag", fontsize=12)
        plt.ylabel("Temperatur (°C)", fontsize=12)
        plt.title("Temperaturvorhersage basierend auf den letzten 10 Wochen", fontsize=16)
        
        # Legende und Gitternetz
        plt.legend()
        plt.grid(axis='y', linewidth=0.5, alpha=0.25)
        
        plt.show()

if __name__ == "__main__":
    # Beispielhafte Verwendung der Klasse
    historische_daten = np.random.uniform(low=9, high=17, size=(10, 7))
    aktuelle_woche = np.random.uniform(10, 17, size=7)
    aktuelle_woche[-3:] = np.nan  # Fr - So noch nicht verfügbar
    
    analysator = TemperaturAnalyse(historische_daten, aktuelle_woche)
    analysator.berechne_statistiken()
    analysator.erstelle_dataframe()
    
    print("\nStatistiken:")
    print(f"Maximale Temperatur: {analysator.max_temp:.2f}°C")
    print(f"Minimale Temperatur: {analysator.min_temp:.2f}°C")
    
    print("\nDataFrame:")
    print(analysator.dataframe)
    
    analysator.plot_daten()
