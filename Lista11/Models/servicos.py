import json
from crud import CRUD

class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.id = id
    self.descricao = descricao
    self.valor = valor
    self.duracao = duracao
  def __str__(self):
    return f"{self.id} | {self.descricao} | R$ {self.valor:.2f} | {self.duracao} min"

class Servicos(CRUD):
    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:  
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:   
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass