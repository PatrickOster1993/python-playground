import requests
import pandas as pd
import tabulate as tb

# Aufgabe 1
""" 
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

if response.status_code == 200:
    print("Lekker bezig amigo")
else:
    print("Try again")
 """
# Aufgabe 2

response2 = requests.get('https://jsonplaceholder.typicode.com/users')

if response2.status_code == 200:
    response2 = response2.json()
    frame = pd.DataFrame(response2)
    print(frame)
else:
    print("Fout bij API aanvraag")