class Equipamento:
    def __init__(self, nome):
        self.nome = nome
        self.estado = "desligado"

    def mostrar_estado(self):
        print("Equipamento: ", self.nome)
        print("Estado: ", self.estado)

    def alterar_estado(self, novo_estado):
        self.estado = novo_estado

equipamento1 = Equipamento("Projetor")
equipamento1.mostrar_estado()
equipamento1.alterar_estado("Ligado")
equipamento1.mostrar_estado()

        