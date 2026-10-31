# 1. Crie uma interface chamada ‘Lapis’ com o método ‘cor’. Crie as classes ‘LapisVerde’, ‘LapisAzul’, ‘LapisVermelho’, que devem implementar a interface e o método herdado mostrando as cores específicas.

from abc import ABC, abstractmethod
class Lapis(ABC):

    @abstractmethod
    def cor (self):
        pass

class LapisVerde(Lapis):
    def cor(self):
        print("Verde")

class LapisAzul(Lapis):
    def cor(self):
        print("Azul")

class LapisVermelho(Lapis):
    def cor(self):
        print("Vermelho")

lapis1 = LapisVerde()
lapis2 = LapisAzul()
lapis3 = LapisVermelho()

lapis1.cor()
lapis2.cor()
lapis3.cor()