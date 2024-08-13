from colorama import Fore, Style, init
from tabulate import tabulate #BIBLIOTECA QUE ORGANIZA LISTA EM TABELAS

class Tenis:

    init()
    lista_tenis = []
    dados_tenis = {}

    #CRIANDO UMA LISTA DE DICIONARIO COM OS DADOS DOS TÊNIS
    def cadastrar(self, tipo=None, marca=None, nome=None, tamanho=None, preco=None):
        self.dados_tenis ["Tipo"] = tipo
        self.dados_tenis ["Marca"] = marca
        self.dados_tenis ["Nome"] = nome
        self.dados_tenis ["Tamanho"] = tamanho
        self.dados_tenis ["Preço"] = preco

        self.lista_tenis.append(self.dados_tenis.copy())
        
        print("Tênis Cadastrado.")

    @classmethod
    def visualizar(cls):
        print(f"==={Fore.GREEN}<<<S N K R S-Meus Tênis>>>{Style.RESET_ALL}===")
       
        #EXIBINDO LISTA EM FORMA DE TABELA
        cabecalhos = cls.lista_tenis[0].keys()

        valores = [tenis.values() for tenis in cls.lista_tenis]

        print(tabulate(valores, headers=cabecalhos, tablefmt="grid"))