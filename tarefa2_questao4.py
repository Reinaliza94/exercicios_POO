numeros = []

for i in range(5):
    n = float(input("Digite um número: "))
    numeros.append(n)

maior = max(numeros)

print(f"O maior número digitado foi: {maior}")