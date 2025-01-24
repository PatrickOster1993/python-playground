"""
Hauptprogramm der CryptoApp.
Initialisiert und startet die MVC-Komponenten.
"""

from models.crypto_model import CryptoModel
from views.crypto_view import CryptoView
from views.chart_view import ChartView
from controllers.crypto_controller import CryptoController

def main():
    """
    Hauptfunktion, die die Anwendung startet.
    Initialisiert Model, Views und Controller und startet die Hauptschleife.
    """
    try:
        # Komponenten initialisieren
        model = CryptoModel()
        view = CryptoView()
        chart_view = ChartView()
        
        # Controller mit den Komponenten erstellen
        controller = CryptoController(model, view, chart_view)
        
        # Anwendung starten
        controller.run()
        
    except Exception as e:
        print(f"Fehler beim Starten der Anwendung: {str(e)}")
        print("Bitte stellen Sie sicher, dass der COINGECKO_API_KEY in den Umgebungsvariablen gesetzt ist.")

if __name__ == "__main__":
    main()