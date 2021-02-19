import requests 

class ValorDoDolar():
    def __init__(self):
        self.values = -1

    def consulta(self):
        url = 'https://economia.awesomeapi.com.br/json/all/USD-BRL'
        retorno = requests.get(url)
        if (retorno.status_code==200):
            jsonparsed = retorno.json()
            self.values = jsonparsed['USD'] ['high']
        else:
            self.Valor = -1