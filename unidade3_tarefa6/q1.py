# 1. Crie uma superclasse chamada ‘Lápis’, com o método ‘cor’, que, ao ser chamado, mostra a cor “preto”. Crie subclasses ‘LapisVerde’, ‘LapisAzul’, ‘LapisVermelho’, que sobrescrevem o método herdado mostrando as cores específicas.


class Lapis:
    def cor (self):
        print("Preto")

class LapisVerde(Lapis):
    def cor(self):
        print("Verde")

class LapisAzul(Lapis):
    def cor (self):
        print("Azul")

class LapisVermelho(Lapis):
    def cor (self):
        print("Vermelho")

lapis_preto = Lapis()
lapis_verde = LapisVerde()
lapis_azul = LapisAzul()
lapis_vermelho = LapisVermelho()

lapis_preto.cor()
lapis_verde.cor()
lapis_azul.cor()
lapis_vermelho.cor()