class Ferramentas:
    def __init__(self):
        self.lista = []

    def adicionar(self, nome): #append
        self.lista.append(nome)

    def listar(self):
        for nome in self.lista:
            print(nome)

    def consultar(self, nome):
        if nome in self.lista:
            print("Ferramenta encontrada")
        else:
            print("Ferramenta não encontrada")

    def remover(self,nome): #remove
        if nome in self.lista:
            self.lista.remove(nome)
        else:
            print("Ferramenta não encontrada")

#Bloco principal
ferramentas = Ferramentas ()

ferramentas.adicionar("VSCode")
ferramentas.adicionar("PyCharm")
ferramentas.adicionar("Git")

ferramentas.listar()
ferramentas.consultar("PyCharm")

####### Segunda Parte #########

ferramentas = Ferramentas()

ferramentas.adicionar("VSCode")
ferramentas.adicionar("Git")

ferramentas.consultar("Eclipse")
ferramentas.remover("VSCode")
ferramentas.listar()

