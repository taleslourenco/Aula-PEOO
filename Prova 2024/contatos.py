import json
from datetime import datetime, date, timedelta


class Contato:
    def __init__(self, id, nome, email, nasc):
        self.id = id
        self.nome = nome
        self.email = email
        self.nasc = nasc
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.nasc}"

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["email"] = self.email
        dic["nasc"] = datetime.strftime(self.nasc, "%d/%m/%Y")
        return(dic)

class Contatos:
    contatos = []
    @classmethod
    def inserir(cls, obj):                #Create
        cls.abrir()                             
        m = 0
        for c in cls.contatos: 
            if c.id > m: m = c.id         #Caso haja ID
        obj.id = m + 1
        cls.contatos.append(obj)
        cls.salvar()

    @classmethod        
    def listar(cls):                      #Read
        cls.abrir()
        return cls.contatos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.contatos:
            if c.id == id: return c
        return None
    
    @classmethod
    def aniversariantes(cls):
        cls.abrir()
        aniversariantes = []
        for c in cls.contatos:
            start_date = datetime(1, 1, 1)
            end_date = datetime(1, 12, 31)
            delta = timedelta(days=1)
            while start_date <= end_date:
                while c.nasc.day == start_date.month:
                    while c.nasc.day == start_date.day:
                        aniversariantes.append(c)
                        start_date += delta
        return aniversariantes
    
    @classmethod
    def atualizar(cls, obj):              #Update
        u = cls.listar_id(obj.id)
        if u != None:
            u.nome = obj.nome
            u.email = obj.email
            u.nasc = obj.nasc
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):                #Remove
        c = cls.listar_id(obj.id)
        if c != None:
            cls.contatos.remove(c)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.contatos = []
        try:
            with open("lista.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Contato(obj["id"], obj["nome"], obj["email"], obj["nasc"])
                    cls.contatos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("lista.json", mode="w") as arquivo:
            json.dump(cls.contatos, arquivo, default = Contato.to_json)

class UI:
    @staticmethod
    def menu():
        print("- 1. Inserir -- 2. Listar -- 3. Atualizar -- 4. Excluir -- 5. Aniversariantes -- 6. Finalizar Programa -")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
            if op == 5: UI.aniversariantes()

    @staticmethod
    def inserir():
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
        nasc = datetime.strptime(nasc, "%d/%m/%Y")
        c = Contato(0, nome, email, nasc)
        Contatos.inserir(c)

    @staticmethod
    def listar(): 
        for c in Contatos.listar():
            print(c)
    
    @staticmethod
    def atualizar():
        UI.listar()
        id = int(input("Informe o id do contato que deseja atualizar: "))
        nome = input("Novo nome: ")
        email = input("Novo email: ")
        nasc = input("Nova data de nascimento (dd/mm/aaaa): ")
        nasc = datetime.strptime(nasc, "%d/%m/%Y")
        c = Contato(id, nome, email, nasc)
        Contatos.atualizar(c)
    
    @staticmethod
    def excluir():
        UI.listar()
        id = int(input("Informe o id do contato que deseja exluir: "))
        c = Contato(id, "", "", "")
        Contatos.excluir(c)

    @staticmethod
    def aniversariantes():
        for c in Contatos.aniversariantes():
            print(c)

UI.main()