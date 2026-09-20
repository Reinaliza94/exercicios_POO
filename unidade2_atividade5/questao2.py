class Cliente:
    def __init__(self, nome, idade, telefone, login, senha):
        self.__nome = nome
        self.__idade = idade
        self.__telefone = telefone
        self.__login = login
        self.__senha = senha

    def alterar_nome(self, novo_nome, senha):
        if senha == self.__senha:
            self.__nome = novo_nome
        else:
            print("Senha incorreta!")

    def alterar_idade(self, nova_idade, senha):
        if senha == self.__senha:
            self.__idade = nova_idade
        else:
            print("Senha incorreta")

    def alterar_telefone(self, novo_telefone, senha):
        if senha == self.__senha:
            self.__telefone = novo_telefone
        else:
            print("Senha incorreta!")

    def alterar_login(self, novo_login, senha):
        if senha == self.__senha:
            self.__login = novo_login
        else:
            print("Senha incorreta!")

    def alterar_senha(self, nova_senha, senha):
        if senha == self.__senha:
            self.__senha = nova_senha
        else:
            print("Senha incorreta!")

    def mostrar_dados(self, senha = None):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")

        if senha == self.__senha:
             print(f"Telefone: {self.__telefone}")
             print(f"Login: {self.__login}")
             print(f"Senha: {self.__senha}")
        else:
            print("Telefone, login e senha: acesso protegido.")

cliente = Cliente ("Ana", 28, 88994949999, "ana12", 123)

cliente.mostrar_dados(123)

cliente.alterar_nome("Carla", 123)
cliente.mostrar_dados(123)

cliente.alterar_idade(32, 123)
cliente.mostrar_dados(123)

cliente.alterar_telefone(8812345678, 123)
cliente.mostrar_dados(123)

cliente.alterar_login("carla12", 123)
cliente.mostrar_dados(123)

cliente.alterar_senha(1234,123)
cliente.mostrar_dados(1234)