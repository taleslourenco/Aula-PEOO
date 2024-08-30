class Viagem:
    def __init__(self):
        self.dist = 0
        self.horas = 0
        self.min = 0
    def veloc(self):
        return self.dist / (self.horas + self.min / 60)
    
x = Viagem()
x.dist = float(input("Insira a distância: "))
x.horas = float(input("Insira o tempo(h): "))
x.min = float(input("Insira o tempo(m): "))
print(f"Velocidade Média: {Viagem.veloc(x)}")