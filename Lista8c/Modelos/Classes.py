import json
from datetime import datetime

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone 
  def __str__(self):
    return f"{self.id} | {self.nome} | {self.email} | {self.fone}"
  
class Horario:
    def __init__(self, id, data, id_cliente, id_servico):
      self.id = id
      self.data = data
      self.confirmado = False
      self.id_cliente = id_cliente
      self.id_servico = id_servico
    def __str__(self):
      return f"{self.id} | {self.data.strftime('%d/%m/%Y %H:%M')}"
    def to_json(self):
      dic = {}
      dic["id"] = self.id
      dic["data"] = self.data.strftime('%d/%m/%Y %H:%M')
      dic["confirmado"] = self.confirmado
      dic["id_cliente"] = self.id_cliente
      dic["id_servico"] = self.id_servico
      return dic

class Servico:
  def __init__(self, id, descricao, valor, duracao):
    self.id = id
    self.descricao = descricao
    self.valor = valor
    self.duracao = duracao
  def __str__(self):
    return f"{self.id} | {self.descricao} | {self.valor} | {self.duracao}"

class Clientes:
  clientes = []  
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0                     
    for c in cls.clientes:     
      if c.id > m: m = c.id  
    obj.id = m + 1  
    cls.clientes.append(obj)
    cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.clientes
  
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.clientes:
      if c.id == id: return c
    return None 
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.email = obj.email
      c.fone = obj.fone
    cls.salvar()   
  
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.clientes.remove(c)
      cls.salvar()   
  
  @classmethod
  def salvar(cls):  
    with open("clientes.json", mode = "w") as arquivo:  
      json.dump(cls.clientes, arquivo, default = vars) 
  
  @classmethod
  def abrir(cls):
    cls.clientes = []
    try: 
      with open("clientes.json", mode = "r") as arquivo:  
        texto = json.load(arquivo)
        for obj in texto:
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     
          cls.clientes.append(c)
    except FileNotFoundError:
      pass

class Horarios:
  horarios = []  
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0                     
    for c in cls.horarios:     
      if c.id > m: m = c.id   
    obj.id = m + 1  
    cls.horarios.append(obj)
    cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.horarios
 
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.horarios:
      if c.id == id: return c
    return None 
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
       c.data = obj.data
       c.confirmado = obj.confirmado
       c.id_cliente = obj.id_cliente
       c.id_servico = obj.id_servico
    cls.salvar()   
  
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.horarios.remove(c)
      cls.salvar()   
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode = "w") as arquivo:   # write
        json.dump(cls.horarios, arquivo, default = Horario.to_json) 
  
  @classmethod
  def abrir(cls):
    cls.horarios = []
    try: 
      with open("horarios.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
            c = Horario(obj["id"], datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
            c.confirmado = obj["confirmado"]
            c.id_cliente = obj["id_cliente"]
            c.id_servico = obj["id_servico"]
            cls.horarios.append(c)
    except FileNotFoundError:
      pass

class Servicos:
  servicos = []  
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0                     
    for c in cls.servicos:     
      if c.id > m: m = c.id   
    obj.id = m + 1  
    cls.servicos.append(obj)
    cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.servicos
  
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.servicos:
      if c.id == id: return c
    return None 
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.descricao = obj.descricao
      c.valor = obj.valor
      c.duracao = obj.duracao
    cls.salvar()   
  
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.servicos.remove(c)
      cls.salvar()   
  
  @classmethod
  def salvar(cls):  
    with open("servicos.json", mode = "w") as arquivo:   
      json.dump(cls.servicos, arquivo, default = vars) 
  
  @classmethod
  def abrir(cls):
    cls.servicos = []
    try: 
      with open("servicos.json", mode = "r") as arquivo:   
        texto = json.load(arquivo)
        for obj in texto:
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])                     
          cls.servicos.append(c)
    except FileNotFoundError:
      pass