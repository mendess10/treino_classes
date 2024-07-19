from cadastro.funcionario import Funcionario

class Verificaon:
    def __init__(self):
        self.dados = Funcionario() #CLASSE FUNCIONARIO
        self.lista_funcionario = self.dados.lista_funcionarios

    #VERIFICAÇÃO DE LOGIN
    def login(self, user, password):
        for usuario in self.lista_funcionario:
            if usuario["Usuario"] == user and usuario["Senha"] == password:
                return True
        return False
