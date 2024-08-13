from pathlib import Path
import sys

caminho_models = Path(__file__).parent.parent
sys.path.append(str(caminho_models))

from models import Tenis

class TenisController():
    
    tenis = Tenis()

    def cadastrar(self, tipo:str, marca:str, nome:str, tamanho:int, preco:int):
        self.tenis.cadastrar(tipo, marca, nome, tamanho, preco)

    def listar(self):
        self.tenis.visualizar()