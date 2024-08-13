from pathlib import Path
import sys

caminho_models = Path(__file__).parent.parent

sys.path.append(str(caminho_models))

from models import Funcionario

class FuncionarioController():
    
    funcionario = Funcionario()

    def cadastrar(self, nome:str, email:str, senha:str):
        self.funcionario.cadastrar(nome, email, senha)

    def listar(self):
        self.funcionario.visualizar()

    def login(self, user:str, password:str):
        return self.funcionario.login(user, password)