from colorama import Fore, Style, init
from tabulate import tabulate #BIBLIOTECA QUE ORGANIZA LISTA EM TABELAS

class Tenis:
    init()
    lista_tenis = []
    
    def __init__(self, tipo=None, marca=None, nome=None, tamanho=None, preco=None): #UTILIZEI None PARA CHAMAR A CLASSE SEM PRECISAR PASSAR OS PARAMETROS
        self.tipo = tipo
        self.marca = marca
        self.nome = nome
        self.tamanho = tamanho
        self.preco = preco
        self.dados_tenis = {}
    #CRIANDO UMA LISTA DE DICIONARIO COM OS DADOS DOS TÊNIS
    def cadastrar_tenis(self):
        self.dados_tenis ["Tipo"] = self.tipo
        self.dados_tenis ["Marca"] = self.marca
        self.dados_tenis ["Nome"] = self.nome
        self.dados_tenis ["Tamanho"] = self.tamanho
        self.dados_tenis ["Preço"] = self.preco
        self.lista_tenis.append(self.dados_tenis.copy())
        print("Tênis Cadastrado.")

    @classmethod
    def visualizar_tenis(cls):
        print(f"==={Fore.GREEN}<<<S N K R S-Meus Tênis>>>{Style.RESET_ALL}===")
        #EXIBINDO LISTA EM FORMA DE TABELA
        cabecalhos = cls.lista_tenis[0].keys()

        valores = [tenis.values() for tenis in cls.lista_tenis]

        print(tabulate(valores, headers=cabecalhos, tablefmt="grid"))