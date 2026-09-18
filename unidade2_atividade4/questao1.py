class Conta:
    def __init__(self, saldo=0.0):
        self.saldo = saldo
    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            print (f"Depósito de {valor} realizado com sucesso!")
        else:
            print("Valor inválido.")
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor <=0:
            print("Valor inválido.")
        else:
            self.saldo -= valor
            print("Saque de", valor, "realizado com sucesso!")
    def mostrar_saldo(self):
        print ("Saldo atual: ", self.saldo)


minha_conta = Conta()

minha_conta.mostrar_saldo()
minha_conta.depositar(100.00)
minha_conta.mostrar_saldo()
minha_conta.sacar(40.00)
minha_conta.mostrar_saldo()
minha_conta.sacar(100.00) 
minha_conta.depositar(-10.00)  
minha_conta.mostrar_saldo()
