import requests
import pandas as pd

def fetch_and_display_users():
    """
    Holt Benutzerdaten von JSONPlaceholder API und zeigt sie strukturiert an
    
    Returns:
        DataFrame: Pandas-DataFrame mit ausgewählten Spalten
    """
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Daten in DataFrame konvertieren
        users_df = pd.json_normalize(response.json())
        
        # Spaltenauswahl und Umbenennung
        selected_columns = ['id', 'name', 'username', 'email']
        filtered_df = users_df[selected_columns]
        
        # DataFrame-Ausgabe
        print("\n🔍 Erhaltene Benutzerdaten:")
        print(filtered_df.to_string(index=False))
        return filtered_df
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Netzwerkfehler: {str(e)}")
    except Exception as e:
        print(f"⚠️ Verarbeitungsfehler: {str(e)}")

if __name__ == "__main__":
    fetch_and_display_users()