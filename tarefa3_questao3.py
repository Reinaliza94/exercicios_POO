class Calculadora:

    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calc = Calculadora()

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

print("Soma:", calc.soma(a, b))
print("Subtração:", calc.sub(a, b))
print("Multiplicação:", calc.multi(a, b))
print("Divisão:", calc.div(a, b))