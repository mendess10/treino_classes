from colorama import Fore, Style, init
from tabulate import tabulate #BIBLIOTECA QUE ORGANIZA LISTA EM TABELAS
class Funcionario:
    init()
    lista_funcionarios = []
    
    def __init__(self, user=None, email=None, senha=None): #UTILIZEI None PARA CHAMAR A CLASSE SEM PRECISAR PASSAR OS PARAMETROS
        self.user = user
        self.email = email
        self.senha = senha
        self.dados = {}
    def cadastrar_funcionario(self):
        #VERIFICANDO SE USUARIO JÁ ESTÁ CADASTRADO
        if any(funcionario["Usuario"] == self.user for funcionario in self.lista_funcionarios):
            print(f"{Fore.LIGHTRED_EX} Usuario já cadastrado{Style.RESET_ALL}")
        #VERIFICANDO SE EMAIL JÁ ESTÁ CADASTRADO
        elif any(funcionario["Email"] == self.email for funcionario in self.lista_funcionarios):
            print(f"{Fore.LIGHTRED_EX}Email já cadastrado.{Style.RESET_ALL}")
        else:
            self.dados ["Usuario"] = self.user
            self.dados ["Email"] = self.email
            self.dados ["Senha"] = self.senha 
            self.lista_funcionarios.append(self.dados.copy())
            print("Funcionario Cadastrado.")

    @classmethod
    def visualizar_funcioanrio(cls):
        print(f"==={Fore.GREEN}<<<S N K R S-Meus Funcionários>>>{Style.RESET_ALL}===")
        #EXIBINDO LISTA EM FORMA DE TABELA
        cabecalhos = cls.lista_funcionarios[0].keys()

        valores = [funcionarios.values() for funcionarios in cls.lista_funcionarios]

        print(tabulate(valores, headers= cabecalhos, tablefmt="grid"))
    