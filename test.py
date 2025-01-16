import datetime
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Make sure all required weather variables are listed here
url = "https://archive-api.open-meteo.com/v1/archive"
start_date = datetime.date.today() - datetime.timedelta(days=70)
end_date = datetime.date.today()

params = {
    "latitude": 51.7667,
    "longitude": 7.95,
    "start_date": start_date,
    "end_date": end_date,
    "hourly": "temperature_2m",
    "temporal_resolution": "hourly_6"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}

hourly_data["temperature_2m"] = hourly_temperature_2m

# Create a DataFrame from the data
hourly_dataframe = pd.DataFrame(data=hourly_data)

# Konvertiere die 'date' Spalte zu einem DatetimeIndex
hourly_dataframe["date"] = pd.to_datetime(hourly_dataframe["date"], utc=True)

# Extrahiere nur die Zeilen, die 12 Uhr an jedem Tag repräsentieren
hourly_dataframe_12pm = hourly_dataframe[hourly_dataframe["date"].dt.hour == 12]

# Füge die Wochentage hinzu
hourly_dataframe_12pm["weekday"] = hourly_dataframe_12pm["date"].dt.day_name()

# Zeige das Ergebnis
print(hourly_dataframe_12pm)

# Definiere die Reihenfolge der Wochentage, beginnend mit Montag
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Füge die benutzerdefinierte Reihenfolge als Kategorie hinzu
hourly_dataframe_12pm['weekday'] = pd.Categorical(hourly_dataframe_12pm['weekday'], categories=weekday_order, ordered=True)

# Gruppiere nach 'weekday' und speichere alle Temperaturwerte als Liste
grouped_data = hourly_dataframe_12pm.groupby("weekday")["temperature_2m"].apply(list)

# Zeige das Ergebnis
print(grouped_data)


# import pandas as pd
# import datetime
# import requests
# from retry_requests import retry
# import requests_cache

# # Setup Open-Meteo API client with cache and retry
# cache_session = requests_cache.CachedSession(".cache", expire_after=-1)
# retry_session = retry(cache_session, retries=5, backoff_factor=0.2)

# # Open-Meteo API endpoint
# url = "https://archive-api.open-meteo.com/v1/archive"

# # Berechne Start- und Enddatum
# end_date = datetime.date.today()
# start_date = end_date - datetime.timedelta(days=70)

# # API-Parameter
# params = {
#     "latitude": 51.7667,  # Münster
#     "longitude": 7.95,
#     "start_date": start_date.strftime("%Y-%m-%d"),
#     "end_date": end_date.strftime("%Y-%m-%d"),
#     "hourly": "temperature_2m",
# }

# # API-Request
# response = retry_session.get(url, params=params)
# response.raise_for_status()  # Sicherstellen, dass die Anfrage erfolgreich war
# data = response.json()

# # Extrahiere die Daten
# hourly_time = data["hourly"]["time"]
# hourly_temperature = data["hourly"]["temperature_2m"]

# # Erstelle ein DataFrame
# df = pd.DataFrame({
#     "datetime": pd.to_datetime(hourly_time),
#     "temperature_2m": hourly_temperature
# })

# # Füge die Wochentage hinzu
# df["weekday"] = df["datetime"].dt.day_name()  # Name des Wochentags
# df["weekday_num"] = df["datetime"].dt.weekday  # Nummer des Wochentags (0=Montag)

# # Optional: Filtere nur 12:00 Uhr pro Tag (falls benötigt)
# df_12pm = df[df["datetime"].dt.hour == 12]

# # Ausgabe
# print(df.head())
# print(df_12pm.head())
