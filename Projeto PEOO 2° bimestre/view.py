from modelo import Fabricante, Veiculo, Modelo, Fabricantes, Veiculos, Modelos

def fabricante_inserir(nome):
    c = Fabricante(0, nome)
    Fabricantes.inserir(c)

def fabricante_listar():
    return Fabricantes.listar()

def fabricante_atualizar(id, nome):
    c = Fabricante(id, nome)
    Fabricantes.atualizar(c)

def fabricante_excluir(id):
    c = Fabricante(id, "")
    Fabricantes.excluir(c)


def veiculo_inserir(nome, id_fabricante):
    c = Veiculo(0, nome, id_fabricante)
    Veiculos.inserir(c)

def veiculo_listar():
    return Veiculos.listar()

def veiculo_atualizar(id, nome, id_fabricante):
    c = Veiculo(id, nome, id_fabricante)
    Veiculos.atualizar(c)

def veiculo_excluir(id):
    c = Veiculo(id, "")
    Veiculos.excluir(c)

def veiculo_contar():
    return Veiculos.contar_veiculos_por_fabricante


def modelo_inserir(nome, cor, id_veiculo):
    c = Modelo(0, nome, cor, id_veiculo)
    Modelos.inserir(c)

def modelo_listar():
    return Modelos.listar()

def modelo_atualizar(id, nome, cor, id_veiculo):
    c = Modelo(id, nome, cor, id_veiculo)
    Modelos.atualizar(c)

def modelo_excluir(id):
    c = Modelo(id, "")
    Modelos.excluir(c)