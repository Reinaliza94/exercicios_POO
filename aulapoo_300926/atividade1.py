class CarteiraDigital:
    def __init__(self, usuario):
        self.usuario = usuario
        self.__saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor #self.__saldo + valor
        else:
            print("Erro: valor inválido")

    def mostrar_saldo(self):
        print("Saldo: ", self.__saldo)

# bloco principal

carteira1 = CarteiraDigital("Glawther")
print(f'Usuário: {carteira1.usuario}')

carteira1.mostrar_saldo()
carteira1.depositar(150000.00)
carteira1.mostrar_saldo()
carteira1.depositar(-1)

            



