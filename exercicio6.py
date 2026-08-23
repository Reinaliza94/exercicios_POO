n = int(input("Digite um número: "))
while n <= 0:
    print("Valor inválido")
    n = int(input("Digite um número: "))
if n > 0:
    print("Valor válido: ", n)