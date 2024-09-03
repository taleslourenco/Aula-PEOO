'''
#ENCAPSULAMENTO

def __init__(self, nome,...):                               #Construir atributo privado
    self.set_variavel(nome)
    ...

def set_variavel(self, nome):
    if nome != "": nome = self.__variavel               #Definir limite 
    else: raise ValueError("qualquer coisa")

def get_variavel(self): return self.__variavel          #Retorna encapsulamento

def __str__(self):
    return f"{self.__variavel} - ..."

def to_json(self):
    dic = {}
    dic["variavel"] = self.__variavel
    ...
    dic["variavel"] = datetime.strftime(self.__variavel, "%d/%m/%Y")

'''