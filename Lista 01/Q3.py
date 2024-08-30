class Conta:
    def __init__(self):
        self.nome = ""
        self.num = 0
        self.saldo = 0
                
    def deposito(self, x):
        x = int(input("Valor do depósito: "))
        return self.saldo + x
    
    def saque(self, x):
        x = int(input("Valor do saque: "))
        return self.saldo - x
    
x = Conta()
x.nome = input("Titular da conta: ")
x.num = int(input("Número da conta: "))
x.saldo = int(input("Saldo da conta: "))
print(f"Saque: {Conta.saque(x)}\nDeposito: {Conta.deposito(x)}")