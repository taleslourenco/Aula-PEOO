from Modelos.Classes import Cliente, Horario, Servico, Clientes, Horarios, Servicos

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

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        obj = Horario(0, data, confirmado, id_cliente, id_servico)
        Horarios.inserir(obj)
      
    def horario_listar():
      return Horarios.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        obj = Horario(id, data, confirmado, id_cliente, id_servico)
        Horarios.atualizar(obj)

    def horario_excluir(id):
        obj = Horario(id, "", "", "", "")
        Horarios.excluir(obj)
        
    def servico_inserir(descricao, valor, duracao):
        obj = Cliente(0, descricao, valor, duracao)
        Clientes.inserir(obj)
      
    def servico_listar():
      return Servicos.listar()

    def servico_atualizar(id, descricao, valor, duracao):
        obj = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(obj)

    def servico_excluir(id):
        obj = Servico(id, "", "", "")
        Servicos.excluir(obj)