class Media:
    def mediaSimples(self, a, b):
        return (a + b) / 2

    def mediaPonderada (self, a, b):
        return (a * 3 + b * 4) / (3 + 4)

Calc = Media()

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Média Simples:", Calc.mediaSimples(a, b))
print("Média Ponderada:", Calc.mediaPonderada(a, b))

