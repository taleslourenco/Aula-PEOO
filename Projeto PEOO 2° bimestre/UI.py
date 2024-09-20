import view

class UI:
    @staticmethod
    def menu():
        print("\n\n== Cadastrar Fabricantes ==\n1 - Inserir\n2 - Listar\n3 - Atualizar\n4 - Excluir\n== Cadastro de Veiculo ==\n5 - Inserir\n6 - Listar\n7 - Atualizar\n8 - Excluir\n9 - Contar Fabricantes\n== Cadastrar Modelo ==\n10 - Inserir\n11 - Listar\n12 - Atualizar\n13 - Excluir\n\n14 - Terminar Programa\n\n")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = 0
        while op != 14:
            op = UI.menu()
            if op == 1: UI.fabricante_inserir()
            if op == 2: UI.fabricante_listar()
            if op == 3: UI.fabricante_atualizar()
            if op == 4: UI.fabricante_excluir()
            if op == 5: UI.veiculo_inserir()
            if op == 6: UI.veiculo_listar()
            if op == 7: UI.veiculo_atualizar()
            if op == 8: UI.veiculo_excluir()
            if op == 9: UI.veiculo_contar()
            if op == 10: UI.modelo_inserir()
            if op == 11: UI.modelo_listar()
            if op == 12: UI.modelo_atualizar()
            if op == 13: UI.modelo_excluir()

    @staticmethod
    def fabricante_inserir():
        nome = input("Informe o nome do fabricante que deseja adicionar: ")
        view.fabricante_inserir(nome)

    @staticmethod
    def fabricante_listar():  
        for c in view.fabricante_listar():
            print(c)
    
    @staticmethod
    def fabricante_atualizar():
        UI.fabricante_listar()
        id = int(input("Informe o id do fabricante que deseja atualizar: "))
        nome = input("Informe o novo nome: ")
        view.fabricante_atualizar(id, nome)

    @staticmethod
    def fabricante_excluir():
        UI.fabricante_listar()
        id = int(input("Informe o id do fabricante que deseja excluir: "))
        view.fabricante_excluir(id)

    @staticmethod
    def veiculo_inserir():
        nome = input("Informe o nome do veículo que deseja adicionar: ")
        UI.fabricante_listar()
        id_fabricante = int(input("Informe o ID do fabricante: "))
        view.veiculo_inserir(nome, id_fabricante)

    @staticmethod
    def veiculo_listar():  
        for c in view.veiculo_listar():
            print(c)
    
    @staticmethod
    def veiculo_atualizar():
        UI.veiculo_listar()
        id = int(input("Informe o ID do veículo que deseja atualizar: "))
        nome = input("Informe o novo nome: ")
        id_fabricante = int(input("Informe o ID do fabricante: "))
        view.veiculo_atualizar(id, nome, id_fabricante)

    @staticmethod
    def veiculo_excluir():
        UI.veiculo_listar()
        id = int(input("Informe o ID do veículo que deseja excluir: "))
        view.veiculo_inserir(id)
    
    @staticmethod
    def veiculo_contar():  
        for c in view.veiculo_contar():
            print(c)

    @staticmethod
    def modelo_inserir():
        nome = input("Informe o nome do modelo que deseja adicionar: ")
        cor = input("Informe a cor: ")
        UI.veiculo_listar
        id_veiculo = int(input("Informe o ID do veiculo: "))
        view.modelo_inserir(nome, id_veiculo)

    @staticmethod
    def modelo_listar():  
        for c in view.modelo_listar():
            print(c)
    
    @staticmethod
    def modelo_atualizar():
        UI.modelo_listar()
        id = int(input("Informe o id do modelo que deseja atualizar: "))
        nome = input("Informe o novo nome: ")
        cor = input("Informe a nova cor: ")
        id_veiculo = int(input("Informe o ID do veiculo: "))
        view.modelo_atualizar(id, nome, cor, id_veiculo)

    @staticmethod
    def modelo_excluir():
        UI.modelo_listar()
        id = int(input("Informe o id do modelo que deseja excluir: "))
        view.veiculo_inserir(id)
 
UI.main()