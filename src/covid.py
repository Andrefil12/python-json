import json, requests

class Cidades():

    def __init__(self):
        self.response

    response = requests.get("https://covid19-brazil-api.now.sh/api/report/v1")

    def estado(self):

        if self.response.status_code == 200:
            print('{} O servidor está disponível'.format(self.response.status_code))
        else:
            print('{} Servidor Indesponível'.format(self.response.status_code))

    def data(self, state, uf, cases, deaths):

        dados = json.loads(self.response.content)

        for dat in dados['data']:
            print("\n")
            print("Estado: {}".format(dat[state]))
            print("UF: {}".format(dat[uf]))
            print("Casos: {}".format(dat[cases]))
            print("Mortes: {}".format(dat[deaths]))
            print("\n")



if __name__ == '__main__':
    cidade = Cidades()
    cidade.estado()
    cidade.data('state','uf','cases','deaths')