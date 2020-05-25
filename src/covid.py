import json, requests

class Cidades():

    def __init__(self):
        self.response

    response = requests.get("https://covid19-brazil-api.now.sh/api/report/v1")

    def estado(self):

        if self.response.status_code == 200:
            print(self.response.status_code + 'O servidor está disponível')
        else:
            print(self.response.status_code + 'Servidor Indesponível')

    dados = json.loads(response.content)

    for dat in dados['data']:
        print(dat['uid'])