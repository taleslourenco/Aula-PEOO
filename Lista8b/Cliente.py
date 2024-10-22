class Cliente:
    def __init__(self, id:int, nome:str, email:str, fone:str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    
    def __str__(self):
        return f"id = {self.__id} | nome = {self.__nome} | email = {self.__email} | fone = {self.__fone}"