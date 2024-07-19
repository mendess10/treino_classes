from colorama import Fore, Style, init
from cadastro.funcionario import Funcionario
from apresentacao.utils import clear_terminal
from verificacoes.check_login import Verificaon
from cadastro.tenis import Tenis

class Screen:
    init()#INICIALIZADOR PARA MUDAR AS CORES DE STRING
    @staticmethod
    def tela_login():
        #LOOP
        while True:
            clear_terminal()
            print(f"""==={Fore.GREEN}<< S N K R S >>{Style.RESET_ALL}===
        [{Fore.GREEN}1{Style.RESET_ALL}]- Cadastrar
        [{Fore.GREEN}2{Style.RESET_ALL}]- Login
        [{Fore.GREEN}3{Style.RESET_ALL}]- Sair
    ===================""")
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
                    clear_terminal()
                    print(f"""==={Fore.GREEN}<<S N K R S - Cadastrar>>{Style.RESET_ALL}===""")
                    user = str(input("Usuario: ")).lower()
                    email = str(input("Email: ")).lower()
                    senha = str(input("Senha: "))
                    #Chamando a classe de funcionario para cadastrar
                    cadastro = Funcionario(user, email, senha) 
                    cadastro.cadastrar_funcionario()
                    input(f"{Fore.GREEN}Pressione enter para continuar...{Style.RESET_ALL}") #PAUSA
                    continue
                case 2:
                    clear_terminal()
                    print(f"==={Fore.GREEN}<<S N K R S - Login>>{Style.RESET_ALL}===")
                    user = str(input("Usuario: "))
                    senha = str(input("Senha: "))
                    validar = Verificaon()
                    #VALIDAÇÃO DE LOGIN
                    if validar.login(user, senha):
                        clear_terminal()
                        Screen.tela_principal()
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
    @staticmethod
    def tela_principal():
        #LOOP
        while True:
            clear_terminal()
            print(f"""==={Fore.GREEN}<<<S N K R S>>>{Style.RESET_ALL}===
        [{Fore.GREEN}1{Style.RESET_ALL}] Cadastrar Tênis
        [{Fore.GREEN}2{Style.RESET_ALL}] Meus Tênis
        [{Fore.GREEN}3{Style.RESET_ALL}] Meus Funcionários
        [{Fore.GREEN}4{Style.RESET_ALL}] Sair
        ===============""")
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
                    cadastro_tenis = Tenis(tipo, marca, nome, tamanho, preco)
                    cadastro_tenis.cadastrar_tenis()
                    input(f"{Fore.GREEN}Pressione enter para continuar...{Style.RESET_ALL}") #PAUSA
                    continue
                case 2:
                    clear_terminal()
                    Tenis.visualizar_tenis()
                    input(f"{Fore.GREEN}Pressione enter para voltar...{Style.RESET_ALL}") #PAUSA
                    continue
                case 3:
                    clear_terminal()
                    Funcionario.visualizar_funcioanrio()
                    input(f"{Fore.GREEN}Pressione enter para voltar...{Style.RESET_ALL}") #PAUSA
                    continue
                case 4:
                    break
                #CASO O USUARIO DIGITE UMA OPÇÃO INVÁLIDA
                case _:
                    print(f"{Fore.LIGHTRED_EX}Digite uma opção válida.{Style.RESET_ALL}")
                    input(f"{Fore.GREEN} Pressione enter para voltar... {Style.RESET_ALL}")
                    continue