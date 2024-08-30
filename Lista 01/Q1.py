class Circulo:
    def __init__(self):
        self.raio: 0
    def area(self):
        return self.raio * 3.14 ** 2
    def circ(self):
        return self.raio * 2 * 3.14 

x = Circulo()
x.raio = float(input("Defina o raio: "))
print(f"area: {Circulo.area(x)}\ncircunferência: {Circulo.circ(x)}")