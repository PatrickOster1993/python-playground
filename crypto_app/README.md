# 🚀 CryptoApp - Kryptowährungs-Analysetool

Eine Python-basierte Anwendung zur Analyse und Visualisierung von Kryptowährungsdaten unter Verwendung der CoinGecko API. Implementiert nach dem Model-View-Controller (MVC) Pattern.

## 📋 Funktionen

- 📊 Aktuelle Kryptowährungspreise abrufen
- 📈 Historische Preisentwicklungen analysieren
- 🔍 Kategorienbasierte Coin-Vergleiche
- 💹 Börsenhandelsdaten untersuchen
- ⚡ Live Bitcoin-Preisdiagramm

## 📊 Klassendiagramm

```mermaid
classDiagram
    class CryptoModel {
        -cg: CoinGeckoAPI
        +__init__()
        -_initialize_client()
        +get_current_prices(coin_ids, currencies)
        +get_historical_data(coin_id, days)
        +get_categories_list()
        +get_coins_in_category(category_id)
        +get_exchanges_list()
        +get_exchange_tickers(exchange_id)
        +get_bitcoin_price()
    }

    class CryptoView {
        +show_menu()
        +get_user_input(prompt)
        +show_prices(prices)
        +show_historical_data(data, coin_id, days)
        +show_categories(categories)
        +show_category_coins(coins, category_id)
        +show_exchanges(exchanges)
        +show_exchange_data(tickers, exchange_id)
    }

    class ChartView {
        -timestamps: deque
        -prices: deque
        -fig: Figure
        -ax: Axes
        -line: Line2D
        +__init__()
        +setup_live_chart(historical_data)
        +update_chart(frame, price)
    }

    class CryptoController {
        -model: CryptoModel
        -view: CryptoView
        -chart_view: ChartView
        +__init__(model, view, chart_view)
        +run()
        -handle_current_prices()
        -handle_historical_data()
        -handle_category_comparison()
        -handle_exchange_analysis()
        -handle_live_chart()
    }

    CryptoController --> CryptoModel : verwendet
    CryptoController --> CryptoView : verwendet
    CryptoController --> ChartView : verwendet
```

## 🔄 Sequenzdiagramm (Live-Chart-Beispiel)

```mermaid
sequenceDiagram
    participant User
    participant Controller as CryptoController
    participant Model as CryptoModel
    participant ChartView
    participant API as CoinGecko API

    User->>Controller: Wählt Live-Chart (Option 5)
    Controller->>Model: get_historical_data('bitcoin', 0.042)
    Model->>API: API-Anfrage für historische Daten
    API-->>Model: Historische Daten
    Model-->>Controller: Historische Daten
    Controller->>ChartView: setup_live_chart(historical_data)
    ChartView->>ChartView: Initialisiere Chart
    
    loop Alle 15 Sekunden
        Controller->>Model: get_bitcoin_price()
        Model->>API: API-Anfrage für aktuellen Preis
        API-->>Model: Aktueller Preis
        Model-->>Controller: Aktueller Preis
        Controller->>ChartView: update_chart(price)
        ChartView->>ChartView: Aktualisiere Visualisierung
        ChartView-->>User: Zeige aktualisiertes Chart
    end
```

## 🏗️ Projektstruktur

```
crypto_app/
├── models/               # Datenmodelle und API-Kommunikation
│   ├── __init__.py
│   └── crypto_model.py
├── views/               # Benutzeroberfläche und Visualisierungen
│   ├── __init__.py
│   ├── crypto_view.py
│   └── chart_view.py
├── controllers/         # Programmsteuerung
│   ├── crypto_controller.py
├── __init__.py
├── main.py             # Hauptprogramm
└── README.md
```

## 🔧 Installation

1. Stellen Sie sicher, dass Python 3.x installiert ist
2. Installieren Sie die erforderlichen Pakete:
```bash
pip install pycoingecko matplotlib
```

3. Setzen Sie Ihren CoinGecko API-Schlüssel als Umgebungsvariable:
```bash
# Windows
set COINGECKO_API_KEY=ihr_api_schlüssel

# Unix/Linux/macOS
export COINGECKO_API_KEY=ihr_api_schlüssel
```

## 🚦 Programmstart

```bash
python main.py
```

## 💻 Nutzung

1. **Aktuelle Preise**
   - Option 1 wählen
   - Coin-IDs eingeben (z.B. bitcoin,ethereum)
   - Währungen eingeben (z.B. usd,eur)

2. **Historische Daten**
   - Option 2 wählen
   - Coin-ID und Zeitraum angeben

3. **Kategorienvergleich**
   - Option 3 wählen
   - Aus verfügbaren Kategorien wählen

4. **Börsenanalyse**
   - Option 4 wählen
   - Börse aus Liste auswählen

5. **Live-Chart**
   - Option 5 wählen
   - Bitcoin-Preis wird live angezeigt

## 🏛️ Architektur

### Model (crypto_model.py)
- Handhabt alle API-Kommunikation
- Verarbeitet und validiert Daten
- Implementiert Geschäftslogik

### Views (crypto_view.py, chart_view.py)
- Benutzerinteraktion via Konsolenschnittstelle
- Datenvisualisierung mit matplotlib
- Formatierte Ausgabe von Informationen

### Controller (crypto_controller.py)
- Koordiniert Model und Views
- Verarbeitet Benutzereingaben
- Steuert Programmablauf

## ⚠️ Fehlerbehandlung

- API-Schlüssel-Validierung
- Netzwerkfehler-Management
- Eingabevalidierung
- Datenqualitätsprüfung

## 🔄 Updates & Wartung

Die MVC-Architektur ermöglicht:
- Einfache Erweiterbarkeit
- Modulare Updates
- Unabhängige Komponententests
- Klare Trennung der Zuständigkeiten

## 📝 Lizenz

MIT License - Siehe LICENSE-Datei für Details.