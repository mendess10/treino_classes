from colorama import Fore, Style, init
from pathlib import Path
import sys
import os

caminho_controller = Path(__file__).parent.parent
print(caminho_controller)
sys.path.append(str(caminho_controller))

from controller import FuncionarioController, TenisController

class Screen():

    init()#INICIALIZADOR PARA MUDAR AS CORES DE STRING
    funcionario_controller = FuncionarioController()
    tenis_controller = TenisController()
    
    @classmethod
    def tela_login(cls):
        #LOOP
        while True:
            cls.clear_terminal()
            print(
                f"==={Fore.GREEN}<< S N K R S >>{Style.RESET_ALL}===\n"
                f" [{Fore.GREEN}1{Style.RESET_ALL}]- Cadastrar\n"
                f" [{Fore.GREEN}2{Style.RESET_ALL}]- Login\n"
                f" [{Fore.GREEN}3{Style.RESET_ALL}]- Sair\n"
                "====================="
            )
            #TRATANDO ERRO DE VALORES
            try:
                opcao = int(input(f"{Fore.GREEN}Insira a opção: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.LIGHTRED_EX}Desculpe, opção digitada está inválida.{Style.RESET_ALL}")
                input(f"{Fore.GREEN}Pressione enter para voltar...{Style.RESET_ALL}")
                continue

            match opcao:
                case 1:
                    #função para limpar terminal anterior
                    cls.clear_terminal()
                    print(f"""==={Fore.GREEN}<<S N K R S - Cadastrar>>{Style.RESET_ALL}===""")
                    user = str(input("Usuario: "))
                    email = str(input("Email: ")).lower()
                    senha = str(input("Senha: "))
                    #Chamando a classe de funcionario para cadastrar
                    cls.funcionario_controller.cadastrar(user, email, senha)
                    input(f"{Fore.GREEN}Pressione enter para continuar...{Style.RESET_ALL}") #PAUSA
                    continue

                case 2:
                    cls.clear_terminal()
                    print(f"==={Fore.GREEN}<<S N K R S - Login>>{Style.RESET_ALL}===")
                    user = str(input("Usuario: "))
                    senha = str(input("Senha: "))

                    #VALIDAÇÃO DE LOGIN
                    if cls.funcionario_controller.login(user, senha):
                        cls.clear_terminal()
                        cls.tela_principal()
                    else:
                        print(f"{Fore.LIGHTRED_EX}Usuario ou Senha incorreto.{Style.RESET_ALL}")
                        input(f"{Fore.GREEN}Pressione enter para continuar...{Style.RESET_ALL}") #PAUSA
                        continue

                case 3:
                    break

                #CASO O USUARIO DIGITE UMA OPÇÃO INVÁLIDA
                case _:
                    print(f"{Fore.LIGHTRED_EX}Digite uma opção válida.{Style.RESET_ALL}")
                    input(f"{Fore.GREEN} Pressione enter para voltar... {Style.RESET_ALL}")
                    continue

    #Criando a tela principal
    @classmethod
    def tela_principal(cls):
        #LOOP
        while True:
            cls.clear_terminal()
            print(
                f"==={Fore.GREEN}<<<S N K R S>>>{Style.RESET_ALL}===\n"
                f"[{Fore.GREEN}1{Style.RESET_ALL}] Cadastrar Tênis\n"
                f"[{Fore.GREEN}2{Style.RESET_ALL}] Meus Tênis\n"
                f"[{Fore.GREEN}3{Style.RESET_ALL}] Meus Funcionários\n"
                f"[{Fore.GREEN}4{Style.RESET_ALL}] Sair\n"
                "====================="
            )
            
            #TRATANDO ERRO DE VALORES
            try:
                opcao = int(input(f"{Fore.GREEN}Insira a opção: {Style.RESET_ALL}"))
            except ValueError:
                print(f"{Fore.LIGHTRED_EX}Desculpe, opção digitada está inválida. {Style.RESET_ALL}")
                input(f"{Fore.GREEN}Pressione enter para voltar...{Style.RESET_ALL}")
                continue

            match opcao:
                case 1:
                    tipo = str(input("Tipo: ")).upper()
                    marca = str(input("Marca: ")).lower()
                    nome = str(input("Nome: ")).lower()
                    tamanho = float(input("Tamanho: "))
                    preco = float(input("Preço: R$"))
                    
                    #CLASSE QUE CADASTRAR OS TENIS 
                    cls.tenis_controller.cadastrar(tipo, marca, nome, tamanho, preco)

                    input(f"{Fore.GREEN}Pressione enter para continuar...{Style.RESET_ALL}") #PAUSA
                    continue

                case 2:
                    cls.clear_terminal()
                    cls.tenis_controller.listar()
                    input(f"{Fore.GREEN}Pressione enter para voltar...{Style.RESET_ALL}") #PAUSA
                    continue
                
                case 3:
                    cls.clear_terminal()
                    cls.funcionario_controller.listar()
                    input(f"{Fore.GREEN}Pressione enter para voltar...{Style.RESET_ALL}") #PAUSA
                    continue
                
                case 4:
                    break
                #CASO O USUARIO DIGITE UMA OPÇÃO INVÁLIDA
                case _:
                    print(f"{Fore.LIGHTRED_EX}Digite uma opção válida.{Style.RESET_ALL}")
                    input(f"{Fore.GREEN} Pressione enter para voltar... {Style.RESET_ALL}")
                    continue

    @staticmethod
    def clear_terminal():
        # Para Windows
        if os.name == 'nt':
            _ = os.system('cls')