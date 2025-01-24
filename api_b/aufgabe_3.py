import requests
import pandas as pd

class APIClient:

    def __init__(self, url_ein):
        try:
            self.__url = url_ein
            self.__response = None # = null / Null / nil
        except Exception as e:
            print("Fehler:", {e})
    
    def getData(self):
        self.__response = requests.get(self.__url)

    def showStructure(self):
        if self.statusCode == 200:
            print(self.__response.text)
        else:
            print("Anfrage an Server nicht erfolgreich!")

    @property
    def responseDict(self):
        if self.statusCode == 200:
            return self.__response.json()
        else:
            return {}
    
    @property
    def responseDf(self):
        return pd.DataFrame(self.responseDict)

    @property
    def statusCode(self):
        return self.__response.status_code
    
client = APIClient(url_ein="https://jsonplaceholder.typicode.com/posts")
client.getData()
print("Antwort im dict-Format:", client.responseDict)
print("Status Code:", client.statusCode)
print("####################################################")
client.showStructure()
print("####################################################")
df = client.responseDf
print(df.head())