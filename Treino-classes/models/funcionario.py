from colorama import Fore, Style, init
from tabulate import tabulate #BIBLIOTECA QUE ORGANIZA LISTA EM TABELAS
class Funcionario:
    init()
    lista_funcionarios = []    
    dados = {}

    def cadastrar(self, user=None, email=None, senha=None):
        #VERIFICANDO SE USUARIO JÁ ESTÁ CADASTRADO
        if any(funcionario["Usuario"] == user for funcionario in self.lista_funcionarios):
            print(f"{Fore.LIGHTRED_EX} Usuario já cadastrado{Style.RESET_ALL}")
        #VERIFICANDO SE EMAIL JÁ ESTÁ CADASTRADO
        elif any(funcionario["Email"] == email for funcionario in self.lista_funcionarios):
            print(f"{Fore.LIGHTRED_EX}Email já cadastrado.{Style.RESET_ALL}")
        else:
            self.dados ["Usuario"] = user
            self.dados ["Email"] = email
            self.dados ["Senha"] = senha 
            self.lista_funcionarios.append(self.dados.copy())
            print("Funcionario Cadastrado.")

    @classmethod
    def visualizar(cls):
        print(f"==={Fore.GREEN}<<<S N K R S-Meus Funcionários>>>{Style.RESET_ALL}===")
        #EXIBINDO LISTA EM FORMA DE TABELA
        cabecalhos = cls.lista_funcionarios[0].keys()

        valores = [funcionarios.values() for funcionarios in cls.lista_funcionarios]

        print(tabulate(valores, headers= cabecalhos, tablefmt="grid"))
    
    def login(self, user, password):
        for usuario in self.lista_funcionarios:
            if usuario["Usuario"] == user and usuario["Senha"] == password:
                return True
        return False