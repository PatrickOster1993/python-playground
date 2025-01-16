import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class TemperaturAnalyse:
    ### Konstruktor ###
    def __init__(self, temperatures, wochentage):
        """
        Initialisiert die Temperaturanalyse mit den gegebenen Temperaturen und Wochentagen.
        """
        self.temperatures = np.array(temperatures)
        self.wochentage = wochentage
        self.mean = None
        self.max_temp = None
        self.min_temp = None
        self.df = None

    def berechne_statistiken(self):
        """
        Berechnet statistische Werte wie Durchschnitt, Maximum und Minimum.
        """
        self.mean = float(np.mean(self.temperatures))
        self.max_temp = float(np.max(self.temperatures))
        self.min_temp = float(np.min(self.temperatures))

    def erstelle_dataframe(self):
        """
        Erstellt einen DataFrame mit den Wochentagen und Temperaturen.
        """
        self.df = pd.DataFrame({
            "Tag": self.wochentage,
            "Temperatur (°C)": self.temperatures
        })

    def plot_temperaturen(self):
        """
        Visualisiert die Temperaturen und hebt Durchschnitt, Maximum und Minimum hervor.
        """
        if self.df is None:
            raise ValueError("DataFrame wurde noch nicht erstellt. Rufen Sie erst 'erstelle_dataframe()' auf.")
        
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        plt.plot(self.df["Tag"], self.df["Temperatur (°C)"], label='Temperatur', color='#F9C0AB', marker='o')

        # Durchschnitt als horizontale Linie
        plt.axhline(y=self.mean, color='#ABE4F9', linestyle=':', label='Durchschnittstemperatur')

        # Achsenbeschriftungen und Titel
        plt.xlabel("Wochentag", fontsize=12)
        plt.ylabel("Temperatur (°C)", fontsize=12)
        plt.title("Temperaturanalyse", fontsize=16)
        plt.legend()
        plt.grid(axis='y', linewidth=0.5, alpha=0.25)

        # Diagramm anzeigen
        plt.show()

    def ausgabe_statistiken(self):
        """
        Gibt die berechneten Statistiken in der Konsole aus.
        """
        print(f"Durchschnittliche Temperatur: {round(self.mean, 2)}°C")
        print(f"Max. Temperatur: {round(self.max_temp, 2)}°C")
        print(f"Min. Temperatur: {round(self.min_temp, 2)}°C")

    def ausgabe_dataframe(self):
        """
        Gibt den DataFrame in der Konsole aus.
        """
        if self.df is None:
            raise ValueError("DataFrame wurde noch nicht erstellt. Rufen Sie erst 'erstelle_dataframe()' auf.")
        print("\nDataFrame:")
        print(self.df)