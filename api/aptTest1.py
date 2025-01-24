import requests

def check_api_status():
    """
    Sendet GET-Anfrage an JSONPlaceholder API und prüft den Statuscode.
    
    Returns:
        bool: True bei Erfolg (Status 200), False bei Fehler
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=5)
        
        # Statuscode Analyse
        if response.status_code == 200:
            print("✅ Erfolg: API-Anfrage erfolgreich (Status 200)")
            return True
        else:
            print(f"⚠️ Warnung: Unerwarteter Statuscode {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Kritischer Fehler: API-Anfrage fehlgeschlagen - {str(e)}")
        return False

if __name__ == "__main__":
    check_api_status()