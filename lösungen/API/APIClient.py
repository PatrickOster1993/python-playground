import requests
import pandas as pd

class APIClient:
    
    def __init__(self, url):
        self.__url = url
        self.__response = None

    def getData(self):
        self.__response = requests.get(self.__url)
        print(self.__response)

    def getDict(self):
        data = self.__response.json()
        print(data)

    def getStatusCode(self):
        statusCode = self.__response.statuscode()
        return statusCode

    def showStructure(self):
        structure = self.__response.text
        print(structure)

    def dataFrame(self):
        dataFrame =  pd.DataFrame(self.__response.json(), columns=["id", "name", "username", "email"])
        print(dataFrame)

Client = APIClient(url='https://jsonplaceholder.typicode.com/users')

Client.getData()
Client.getDict()
