import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TemperaturAnalyse:
    def __init__(self, former_temperature, current_temperature):
        self.former_temperature = former_temperature
        self.current_temperature = current_temperature
        self.days = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
        self.average_temperatures = None
        self.max_temp = None
        self.min_temp = None
        self.df = None

    def berechne_durchschnittstemperaturen(self):
        self.average_temperatures = np.mean(self.former_temperature, axis=0)
        self.max_temp = np.max(self.average_temperatures)
        self.min_temp = np.min(self.average_temperatures)

    def erstelle_dataframe(self):
        df_dict = {
            "Tag": self.days,
            "Durchschnittstemperatur (°C)": self.average_temperatures
        }
        self.df = pd.DataFrame(df_dict)

    def zeige_dataframe(self):
        print("\nDataFrame:")
        print(self.df)

    def plotte_diagramm(self):
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        plt.plot(self.df["Tag"], self.df["Durchschnittstemperatur (°C)"], label='Durchschnittstemperatur', color='#ABE4F9')
        plt.plot(self.df["Tag"], self.current_temperature, label='Aktuelle Woche', color='#F9E7AB')

        plt.axhline(y=self.max_temp, color='#ABF9E7', linestyle=':', label='Max. Temperatur')
        plt.axhline(y=self.min_temp, color='#F9ABBD', linestyle=':', label='Min. Temperatur')

        plt.xlabel("Wochentag", fontsize=12)
        plt.ylabel("Temperatur (°C)", fontsize=12)
        plt.title("Temperaturvorhersage basierend auf den letzten 10 Wochen", fontsize=16)

        plt.legend()
        plt.grid(axis='y', linewidth=0.5, alpha=0.25)

        plt.show()

    def analysiere(self):
        self.berechne_durchschnittstemperaturen()
        self.erstelle_dataframe()
        self.zeige_dataframe()
        self.plotte_diagramm()

# Beispielverwendung:
former_temperature = np.random.uniform(low=9, high=17, size=(10, 7))
current_temperature = np.random.uniform(10, 17, size=7)
current_temperature[-3:] = np.nan

analyse = TemperaturAnalyse(former_temperature, current_temperature)
analyse.analysiere()
