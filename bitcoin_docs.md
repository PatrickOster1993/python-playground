# Bitcoin Preis Monitor Dokumentation

## Projektübersicht
Dieses Python-Skript zeigt den aktuellen Bitcoin-Preis in Echtzeit an und visualisiert die Preisentwicklung in einem Diagramm. Es verwendet die CoinGecko API für Preisabfragen und Matplotlib für die Visualisierung.

## Installation

### Voraussetzungen
- Python 3.8 oder höher
- Installierte Pakete: `requests`, `matplotlib`, `pandas`

### Installation
1. Python installieren: [python.org](https://www.python.org/)
2. Abhängigkeiten installieren:
```bash
pip install requests matplotlib pandas
```

## API-Referenz

### `fetch_bitcoin_price()`
Ruft den aktuellen Bitcoin-Preis von der CoinGecko-API ab.

**Rückgabewert:**
- `float`: Aktueller Preis in USD
- `None`: Bei Fehlern

### `update(frame)`
Aktualisiert das Diagramm und die Preisliste.

**Parameter:**
- `frame`: Animationsframe (wird von FuncAnimation verwendet)

## Code-Erklärungen

### Konfiguration
```python
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price..."
```
Die API-URL für Preisabfragen.

### Datenstrukturen
```python
timestamps = deque(maxlen=100)
prices = deque(maxlen=100)
```
Speichert die letzten 100 Zeitstempel und Preise.

### Diagramm Initialisierung
```python
fig, ax = plt.subplots()
line, = ax.plot([], [], label="Bitcoin Preis (USD)")
```
Erstellt das Diagramm mit Achsenbeschriftungen und Legende.

## Beispielanwendung
```python
# Startet die Echtzeit-Anzeige
plt.show()
```

## Fehlerbehandlung
Das Skript enthält umfangreiche Fehlerbehandlung für:
- API-Aufrufe
- Datenverarbeitung
- Diagrammaktualisierung

## Lizenz
MIT License - Siehe [LICENSE](LICENSE) Datei für Details.

## Kontakt
Für Fragen oder Anregungen kontaktieren Sie bitte den Projektbetreuer.
