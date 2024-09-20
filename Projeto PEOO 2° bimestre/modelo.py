import json

class Fabricante:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"Fabricante(id={self.id}, nome='{self.nome}')"
    
class Veiculo:
    def __init__(self, id, nome, id_fabricante):
        self.id = id
        self.nome = nome
        self.id_fabricante = id_fabricante

    def __str__ (self):
        return f"Veiculo(id = {self.id}), nome ='{self.nome}', Fabricante(id = {self.id_fabricante})"
    
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["nome"] = self.nome
      dic["id_fabricante"] = self.id_fabricante
      return dic   

class Modelo:
    def __init__(self, id, nome, cor, id_veiculo):
        self.id = id
        self.nome = nome
        self.cor = cor
        self.id_veiculo = id_veiculo

    def __str__(self):
        return f"Modelo(id = {self.id}), nome ='{self.nome}', cor ='{self.cor}', Veículo(id = {self.id_veiculo})"

    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["nome"] = self.nome
      dic["cor"] = self.cor
      dic["id_veiculo"] = self.id_veiculo
      return dic 
   
class Fabricantes:
    fabricantes = []  # Lista que simula um banco de dados
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.fabricantes:
            if c.id > m: 
                m = c.id
        obj.id = m + 1
        cls.fabricantes.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.fabricantes
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.fabricantes:
            if c.id == id: return c
        return None
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.fabricantes.remove(c)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("fabricantes.json", mode="w") as arquivo:   # w - write
            json.dump(cls.fabricantes, arquivo, default = vars)
    
    @classmethod
    def abrir(cls):
        cls.fabricantes = []
        try:
            with open("fabricantes.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Fabricante(obj["id"], obj["nome"])
                    cls.fabricantes.append(c)
        except FileNotFoundError:
            pass

class Veiculos:
    veiculos = []  # Lista que simula um banco de dados
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.veiculos:
            if c.id > m: 
                m = c.id
        obj.id = m + 1
        cls.veiculos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.veiculos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.veiculos:
            if c.id == id: return c
        return None
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.id_fabricante = obj.id_fabricante
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.veiculos.remove(c)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("veiculos.json", mode="w") as arquivo:  
            json.dump(cls.veiculos, arquivo, default = Veiculo.to_json)
    
    @classmethod
    def abrir(cls):
        cls.veiculos = []
        try:
            with open("veiculos.json", mode="r") as arquivo:   
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Veiculo(obj["id"], obj["nome"], obj["id_fabricante"])
                    cls.veiculos.append(c)
        except FileNotFoundError:
            pass
    
    @classmethod
    def contar_veiculos_por_fabricante(cls):
        contagem = {}
        for veiculo in cls.veiculos:
            fabricante_id = veiculo.id_fabricante
            if fabricante_id not in contagem:
                contagem[fabricante_id] = 0
            contagem[fabricante_id] += 1
        return contagem

class Modelos:
    modelos = []  
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for c in cls.modelos:
            if c.id > m: 
                m = c.id
        obj.id = m + 1
        cls.modelos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.modelos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for c in cls.modelos:
            if c.id == id: return c
        return None
    
    @classmethod
    def atualizar(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.cor = obj.cor
            c.id_veiculo = obj.id_veiculo
            cls.salvar()
    
    @classmethod
    def excluir(cls, obj):
        c = cls.listar_id(obj.id)
        if c != None:
            cls.modelos.remove(c)
            cls.salvar()

    @classmethod
    def salvar(cls):
        with open("modelos.json", mode="w") as arquivo:   
            json.dump(cls.modelos, arquivo, default = Modelo.to_json)
    
    @classmethod
    def abrir(cls):
        cls.modelos = []
        try:
            with open("modelos.json", mode="r") as arquivo:   
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Modelo(obj["id"], obj["nome"], obj["cor"], obj["id_veiculo"])
                    cls.modelos.append(c)
        except FileNotFoundError:
            pass