class Pessoa ():
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

input_nome = input("Digite o nome da pessoa: ")
input_idade = int(input("Digite a idade da pessoa: "))
input_altura = float(input("Digite a altura da pessoa: "))

pessoa = Pessoa(input_nome, input_idade, input_altura)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Altura: {pessoa.altura}")