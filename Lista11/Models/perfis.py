import json
from CRUD import CRUD

class Perfil:
    def __init__(self, id, nome, descricao, beneficios):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios
  
    def __str__(self):
        return f"{self.nome} | {self.descricao} | {self.beneficios}"

class Perfis(CRUD):
    @classmethod
    def salvar(cls):
        with open("perfis.json", mode="w") as arquivo:  
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("perfis.json", mode="r") as arquivo:   
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Perfil(obj["id"], obj["nome"], obj["edescricao"], obj["beneficios"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass