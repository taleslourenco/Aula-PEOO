from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = ""
        self.__cpf = ""
        self.__telefone = ""
        self.__nascimento = datetime()
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_nome(self, x):
        if x != "": x = self.__nome
        else: raise ValueError()
    def set_cpf(self, x):
        if x != "": x = self.__cpf
        else: raise ValueError()
    def set_telefone(self, x):
        if x != "": x = self.__telefone
        else: raise ValueError()
    def set_nascimento(self, x):
        if x < datetime.now(): x = self.__nascimento
        else: raise ValueError()
    
    def get_nome(self):
        return self.__nome
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento

    def idade(self):
        hj = datetime.now()
        idade = hj - self.__nascimento
        dias = idade.days
        mes = dias / 30
        ano = dias / 365
        return f"anos: {ano} - mes: {mes}"
        
    def __str__(self):
        return f"`{self.__nome}, {self.__cpf}, {self.__telefone}, {self._nascimento.strftime("%d/%m%Y")}"