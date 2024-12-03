class Perfil:
    def __init__(self, id, nome, descricao, beneficios):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.beneficios = beneficios
  
    def __str__(self):
        return f"{self.nome} | {self.descricao} | {self.beneficios}"