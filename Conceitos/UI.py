'''
#CLASSE UI

@staticmethod
def menu():
    print("1 - ação")
    return int(input("Informe uma opção: "))

@staticmethod
def main():
    op = 0
    while op != (o número que finaliza o programa):
      op = UI.menu()
      if op == 1: UI.função respectiva da UI
      ...

@staticmethod
def paciente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    fone = input("Informe o fone: ")
    nasc = input("Informe a data de nascimento (dd/mm/aaaa): ")
    nasc = datetime.strptime(nasc, "%d/%m/%Y")
    p = Paciente(0, nome, fone, nasc)
    NPaciente.inserir(p)

@staticmethod
def paciente_listar():  
    for p in NPaciente.listar():
      print(p)

@staticmethod
def paciente_atualizar():
    UI.paciente_listar()
    id = int(input("Informe o id do paciente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    fone = input("Informe o novo fone: ")
    nasc = input("Informe a nova data de nascimento (dd/mm/aaaa): ")
    nasc = datetime.strptime(nasc, "%d/%m/%Y")
    p = Paciente(id, nome, fone, nasc)
    NPaciente.atualizar(p)

@staticmethod
def paciente_excluir():
    UI.paciente_listar()
    id = int(input("Informe o id do paciente a ser excluído: "))
    p = Paciente(id, "", "", "")
    NPaciente.excluir(p)

@staticmethod
def aniversariantes():
    mes = int(input("Mês dos aniversariantes: "))
    a = NPaciente.aniversariantes(NPaciente, mes)
    for x in a:
      print(x)

UI.main()
'''