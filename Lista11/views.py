from Models.clientes import Cliente, Clientes
from Models.horarios import Horario, Horarios
from Models.servicos import Servico, Servicos
from Models.perfis import Perfil, Perfis
from Models.profissionais import Profissional, Profissionais
from datetime import datetime, timedelta

class View:
    #CLIENTE
    def cliente_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234", 1)

    def cliente_inserir(nome, email, fone, senha, id_perfil):
        c = Cliente(0, nome, email, fone, senha, id_perfil)
        Clientes.inserir(c)

    def cliente_listar():
        return Clientes.listar()    

    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    def cliente_atualizar(id, nome, email, fone, senha, id_perfil):
        c = Cliente(id, nome, email, fone, senha, id_perfil)
        Clientes.atualizar(c)

    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "", 0)
        Clientes.excluir(c)    

    #PERFIL
    def perfil_inserir(nome, descricao, beneficios):
        c = Perfil(0, nome, descricao, beneficios)
        Perfis.inserir(c)

    def perfil_listar():
        return Perfis.listar()    

    def perfil_listar_id(id):
        return Perfis.listar_id(id)    

    def perfil_atualizar(id, nome, descricao, beneficios):
        c = Perfil(id, nome, descricao, beneficios)
        Perfis.atualizar(c)

    def perfil_excluir(id):
        c = Perfil(id, "", "", "")
        Perfis.excluir(c)    


    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None

    #HORÁRIO
    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.inserir(c)

    def horario_listar():
        return Horarios.listar()    

    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.id_cliente == None: disponiveis.append(h)
        return disponiveis   

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.confirmado = confirmado
        c.id_cliente = id_cliente
        c.id_servico = id_servico
        Horarios.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        Horarios.excluir(c)    

    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        dt = datetime.strptime(data, "%d/%m/%Y")
        if dt.date() < datetime.now().date(): 
            raise ValueError("Data não pode estar no passado")
        if intervalo > 120: 
            raise ValueError("Intervalo máximo é 120 min")

        #data = "05/11/2024"
        #inicio = "08:00"
        #fim = "12:00"
        #intervalo = 60
        i = data + " " + hora_inicio   # "05/11/2024 08:00"
        f = data + " " + hora_fim      # "05/11/2024 12:00"
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            #cadastrar o horário x
            View.horario_inserir(x, False, None, None)
            #passar para o próximo horário
            x = x + d

    #SERVIÇO
    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    def servico_listar():
        return Servicos.listar()    

    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    def servico_excluir(id):
        c = Servico(id, "", 0, 0)
        Servicos.excluir(c)
    
    #PROFISSIONAL
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        c = Profissional(0, nome, especialidade, conselho, email, senha)
        Profissionais.inserir(c)

    def profissional_listar():
        return Profissionais.listar()    

    def profissional_listar_id(id):
        return Profissionais.listar_id(id)    

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        c = Profissional(id, nome, especialidade, conselho, email, senha)
        Profissionais.atualizar(c)

    def profissional_excluir(id):
        c = Profissional(id, "", "", "", "", "")
        Profissionais.excluir(c) 
