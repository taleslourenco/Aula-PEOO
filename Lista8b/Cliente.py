class Cliente:
    def __init__(self, id:int, nome:str, email:str, fone:str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    
    def __str__(self):
        return f"id = {self.id} | nome = {self.nome} | email = {self.email} | fone = {self.fone}"