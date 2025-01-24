import pandas as pd
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = pd.DataFrame(response.json(), columns=["id", "name", "username", "email"]).set_index('id')
# users = pd.DataFrame(response.json())[['id', 'name', 'username', 'email']].set_index('id')

print(users)