# 3. Crie uma classe abstrata chamada ‘Objeto3D’, com o atributo ‘altura’, o método abstrato ‘areaBase’ e o método concreto ‘volume’. Esse último retorna o cálculo de volume: (areaBase * altura). Crie as subclasses ‘Cilindro’ e ‘Retangulo’ e desenvolva, em cada uma, o método herdado ‘areaBase’. Depois teste o método ‘volume’ de cada.


from abc import ABC, abstractmethod

class Objeto3D(ABC):
    def __init__(self, altura):
        self.altura = altura

    @abstractmethod
    def areaBase(self):
        pass

    def volume(self):
        return self.areaBase() * self.altura


class Cilindro(Objeto3D):
    def __init__(self, altura, raio):
        super().__init__(altura)
        self.raio = raio

    def areaBase(self):
        return 3.14 * self.raio ** 2


class Retangulo(Objeto3D):
    def __init__(self, altura, largura, comprimento):
        super().__init__(altura)
        self.largura = largura
        self.comprimento = comprimento

    def areaBase(self):
        return self.largura * self.comprimento


cilindro = Cilindro(10, 3)
retangulo = Retangulo(5, 4, 6)

print("Volume do cilindro:", cilindro.volume())
print("Volume do retângulo:", retangulo.volume())