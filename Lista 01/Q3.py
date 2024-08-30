class Conta:
    def __init__(self):
        self.nome = ""
        self.num = 0
        self.saldo = 0

                
    def deposito(self, y):
        return self.saldo + y
    
    def saque(self, y):
        return self.saldo - y
    
x = Conta()
x.nome = input("Titular da conta: ")
x.num = int(input("Número da conta: "))
x.saldo = int(input("Saldo da conta: "))
y = int(input("Digite o valor para depositar/sacar: "))
print(f"Saque: {x.saque(y)}\nDeposito: {x.deposito(y)}")