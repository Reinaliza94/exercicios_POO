class Lampada:
    def __init__(self, estado_inicial: bool):
        self.ligada = estado_inicial

    def setStatus(self, novo_estado: bool):
        self.ligada = novo_estado

    def showStatus(self):
        if self.ligada:
            print("A lâmpada está ligada.")
        else:
            print("A lâmpada está desligada.")

minha_lampada = Lampada(True)
minha_lampada.showStatus()
minha_lampada.setStatus(False)
minha_lampada.showStatus()