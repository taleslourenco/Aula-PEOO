import json
from CRUD import CRUD

class Cliente:
    def __init__(self, id, nome, email, fone, senha, id_perfil):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
        self.id_perfil = id_perfil
    def __str__(self):
        return f"{self.nome} | {self.email} | {self.fone} | {self.id_perfil}"

class Clientes(CRUD):
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:  
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:   
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"], obj["id_perfil"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass