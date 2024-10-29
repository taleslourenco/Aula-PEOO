from Lista8c.Models.classe import Cliente, Horario, Servico, Clientes, Horarios, Servicos

class View:
    def cliente_inserir(nome, email, fone):
        obj = Cliente(0, nome, email, fone)
        Clientes.inserir(obj)
      
    def cliente_listar():
      return Clientes.listar()

    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        Clientes.atualizar(obj)

    def cliente_excluir(id):
        obj = Cliente(id, "", "", "")
        Clientes.excluir(obj)

    def horario_inserir(data):
        obj = Horario(0, data)
        Horarios.inserir(obj)
      
    def horario_listar():
      return Horarios.listar()

    def horario_atualizar(id, data):
        obj = Horario(id, data)
        Horarios.atualizar(obj)

    def horario_excluir(id):
        obj = Horario(id, "")
        Horarios.excluir(obj)
        
    def servico_inserir(descricao, valor, duracao):
        obj = Servico(0, descricao, valor, duracao)
        Servicos.inserir(obj)
      
    def servico_listar():
      return Servicos.listar()

    def servico_atualizar(id, descricao, valor, duracao):
        obj = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(obj)

    def servico_excluir(id):
        obj = Servico(id, "", "", "")
        Servicos.excluir(obj)