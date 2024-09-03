'''
#CRUD = Create, Read, Update, Delete

class #nome:
lista = []

@classmethod
def inserir(cls, obj):                #Create
    cls.abrir()                             
    m = 0
    for p in cls.lista: 
        if p.id > m: m = p.id         #Caso haja ID
    obj.id = m + 1
    cls.lista.append(obj)
    cls.salvar()

@classmethod        
def listar(cls):                      #Read
    cls.abrir()
    return cls.lista

@classmethod
def listar_id(cls, id):
    cls.abrir()
    for p in cls.lista:
      if p.id == id: return p
    return None  

@classmethod
def atualizar(cls, obj):              #Update
    h = cls.listar_id(obj.id)
    if h != None:
      h.nome = obj.nome
      h.fone = obj.fone
      h.nasc = obj.nasc
      cls.salvar()

@classmethod
def excluir(cls, obj):                #Remove
    p = cls.listar_id(obj.id)
    if p != None:
      cls.lista.remove(p)
    cls.salvar()

@classmethod
def salvar(cls):
    with open("lista.json", mode="w") as arquivo:
      json.dump(cls.lista, arquivo, default = (classe construtora).to_json)

@classmethod
def abrir(cls):
    cls.lista = []
    try:
      with open("lista.json", mode="r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:   
          p = Classe construtora(obj["id"], obj["nome"], obj["fone"], obj["nasc"])
          cls.lista.append(p)
    except FileNotFoundError:
      pass
'''