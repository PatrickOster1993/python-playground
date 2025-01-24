"""
Controller-Komponente für die Koordination zwischen Model und Views.
Handhabt die Programmlogik und Benutzerinteraktionen.
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class CryptoController:
    def __init__(self, model, view, chart_view):
        """
        Initialisiert den Controller mit Model- und View-Instanzen.
        
        Args:
            model: CryptoModel Instanz
            view: CryptoView Instanz
            chart_view: ChartView Instanz
        """
        self.model = model
        self.view = view
        self.chart_view = chart_view
    
    def run(self):
        """Hauptprogrammschleife"""
        while True:
            self.view.show_menu()
            choice = self.view.get_user_input("Bitte wählen Sie eine Option (1-6): ")
            
            if choice == '1':
                self.handle_current_prices()
            elif choice == '2':
                self.handle_historical_data()
            elif choice == '3':
                self.handle_category_comparison()
            elif choice == '4':
                self.handle_exchange_analysis()
            elif choice == '5':
                self.handle_live_chart()
            elif choice == '6':
                print("Programm wird beendet.")
                break
            else:
                print("Ungültige Auswahl, bitte versuchen Sie es erneut.")
    
    def handle_current_prices(self):
        """Verarbeitet Preisabfragen"""
        coins = self.view.get_user_input(
            "Geben Sie die IDs der Kryptowährungen ein (durch Kommas getrennt): "
        )
        currencies = self.view.get_user_input(
            "Geben Sie die Vergleichswährungen ein (durch Kommas getrennt): "
        )
        prices = self.model.get_current_prices(coins.split(','), currencies.split(','))
        self.view.show_prices(prices)
    
    def handle_historical_data(self):
        """Verarbeitet historische Datenabfragen"""
        coin_id = self.view.get_user_input("Geben Sie die ID der Kryptowährung ein: ")
        days = self.view.get_user_input("Geben Sie die Anzahl der Tage ein: ")
        data = self.model.get_historical_data(coin_id, days)
        self.view.show_historical_data(data, coin_id, days)
    
    def handle_category_comparison(self):
        """Verarbeitet Kategorienvergleiche"""
        try:
            categories = self.model.get_categories_list()
            self.view.show_categories(categories)
            category_id = self.view.get_user_input(
                "Geben Sie die ID der gewünschten Kategorie ein: "
            )
            coins = self.model.get_coins_in_category(category_id)
            self.view.show_category_coins(coins, category_id)
        except Exception as e:
            print(f"Fehler beim Kategorievergleich: {str(e)}")
    
    def handle_exchange_analysis(self):
        """Verarbeitet Börsenanalysen"""
        exchanges = self.model.get_exchanges_list()
        self.view.show_exchanges(exchanges)
        exchange_id = self.view.get_user_input(
            "Geben Sie die ID der gewünschten Börse ein: "
        )
        tickers = self.model.get_exchange_tickers(exchange_id)
        self.view.show_exchange_data(tickers, exchange_id)
    
    def handle_live_chart(self):
        """Verarbeitet Live-Chart-Anzeige"""
        historical_data = self.model.get_historical_data('bitcoin', 0.042)
        fig, ax, line = self.chart_view.setup_live_chart(historical_data)
        
        def update(frame):
            price = self.model.get_bitcoin_price()
            self.chart_view.update_chart(frame, price)
        
        print("Live Bitcoin-Preisdiagramm wird gestartet...")
        ani = FuncAnimation(fig, update, interval=15000)
        plt.show()