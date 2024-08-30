class Cinema:
    def __init__(self):
        self.dia = ""
        self.hora = 0
    
    def Inteiro(self):
        if self.dia == "segunda" or self.dia == "terça" or self.dia =="quinta":
            if self.hora < 17:
                return "R$ 16,00"
            else: 
                return "R$ 24,00"
        
        if self.dia == "sexta" or self.dia == "sábado" or self.dia =="domingo":
            if self.hora < 17:
                return "R$ 20,00"
            else: 
                return "R$ 30,00"
    
    def Meia(self):
        print(Cinema.Inteiro(self) / 2)
        if self.dia == "quarta":
            if self.hora < 17:
                return "R$ 8,00" 
            else:
                return"R$ 12,00"

x = Cinema()
x.dia = input("Informe o dia da semana: ")
x.hora = int(input("Informe a hora: "))
print(f"inteiro: {Cinema.Inteiro(x)}\nmeia: {Cinema.Meia(x)}")