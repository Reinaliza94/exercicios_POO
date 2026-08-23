class Produto:
    def __init__(self, nome, marca, peso, quantia):
        self.nome = nome
        self.marca = marca
        self.peso = peso
        self.quantia = quantia

# Produto 1

print("\nDigite os dados do produto 1:")
nome = input("Nome: ")
marca = input("Marca: ")
peso = float(input("Peso: "))
quantia = int(input("Quantia: "))

produto1 = Produto(nome, marca, peso, quantia)  

# Produto 2

print("\nDigite os dados do produto 2:")
nome = input("Nome: ")
marca = input("Marca: ")
peso = float(input("Peso: "))
quantia = int(input("Quantia: "))

produto2 = Produto(nome, marca, peso, quantia)

# Produto 3

print("\nDigite os dados do produto 3:")
nome = input("Nome: ")
marca = input("Marca: ")
peso = float(input("Peso: "))
quantia = int(input("Quantia: "))

produto3 = Produto(nome, marca, peso, quantia)


#Exibir os dados dos produtos

print("\nDados do Produto 1:")
print(f"Nome: {produto1.nome}")
print(f"Marca: {produto1.marca}")
print(f"Peso: {produto1.peso}") 
print(f"Quantia: {produto1.quantia}")

print("\nDados do Produto 2:")
print(f"Nome: {produto2.nome}")
print(f"Marca: {produto2.marca}")
print(f"Peso: {produto2.peso}")
print(f"Quantia: {produto2.quantia}")


print("\nDados do Produto 3:")
print(f"Nome: {produto3.nome}")
print(f"Marca: {produto3.marca}")
print(f"Peso: {produto3.peso}")
print(f"Quantia: {produto3.quantia}")

