import json
from crud import CRUD

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
        self.email = email
        self.senha = senha
    def __str__(self):
        return f"{self.nome} | {self.especialidade} | {self.conselho} | {self.email}"

class Profissionais(CRUD):
    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:  
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:   
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"], obj["email"], obj["senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass