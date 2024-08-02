class Jogador:
    def __init__(self):
        self.__nome = ""
        self.__camisa = 0
        self.__gols = 0
    def set_nome(self, x):
        if x != "": self.__nome = x
        else: raise ValueError
    def set_camisa(self, x):
        if x > 0: self.__camisa = x
    def set_gols(self, x):
        if x >= 0: self.__gols = x

    def get_nome(self):
        return self.__nome
    def get_camisa(self):
        return self.__camisa
    def get_gols(self):
        return self.__gols

    def __str__(self):
        return (f"Nome: {self.__nome}\nCamisa: {self.__camisa}\nGols: {self.__gols}")
    
class Time:
    def __init__(self):
        self.__nome = ""
        self.__estado = ""
        self.__jogadores = []
    def set_nome(self, x):
        if x != "": self.__nome = x
        else: raise ValueError
    def set_estado(self, x):
        if x != "": self.__estado = x
        else: raise ValueError

    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    
    def inserir(self, jogador):
        self.__jogadores.append(jogador)
    
    def listar(self):
        for jogador in self.__jogadores:
            print(jogador)
    
    def artilheiro(self):
        return max(self.__jogadores, key = lambda jogador: jogador.get_gols())

    def __str__(self):
        return(f"Nome do time: {self.__nome}\nEstado: {self.__estado}\nJogadores: {self.__jogadores}")

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: time = UI.criar_time()
            if op == 2: UI.inserir_jogadores(time)
            if op == 2: UI.listar_jogadores()
            if op == 2: UI.artilheiro()

    @staticmethod
    def menu():
        print("1. Criar um time\n2. Inserir Jogadores\n3. listar jogadores\n4. Artilheiro")
        return int(input("Digite um número: "))

    @staticmethod
    def criar_time():
        time = Time()
        time.set_nome(input('Nome:'))
        time.set_estado = input("Estado: ")
        return time



    @staticmethod
    def inserir_jogadores(time):
        jogador = Jogador()
        jogador.set_nome = input("Nome do jogador: ")
        jogador.set_camisa = int(input("Número da camisa: "))
        jogador.set_gols = int(input("Número de gols: "))
        time.inserir(jogador)

    @staticmethod
    def listar_jogadores():
    

    @staticmethod
    def artilheiro():







    

