import os
# Função que limpa a tela no terminal
def clear_terminal():
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')