# 2. Crie uma classe abstrata chamada ‘Semaforo’, com o método abstrato chamado ‘mudar’, cujo propósito é alterar a cor da luz do semáforo. Agora crie uma classe ‘SemaforoPlus’, que herda da classe abstrata e implementa seu método de mudar cor, seguindo a sequência verde -> vermelho -> amarelo, aqui retomando ao início da sequência. Adicione ainda nessa subclasse o método ‘emergencia’, que mostra a cor azul, em caso de defeito.


from abc import ABC, abstractmethod

class Semaforo(ABC):
    def __init__(self):
        self.cor_atual = "Verde"

    @abstractmethod
    def mudar(self):
        pass


class SemaforoPlus(Semaforo):

    def mudar(self):
        if self.cor_atual == "Verde":
            self.cor_atual = "Vermelho"

        elif self.cor_atual == "Vermelho":
            self.cor_atual = "Amarelo"

        elif self.cor_atual == "Amarelo":
            self.cor_atual = "Verde"

        print(self.cor_atual)

    def emergencia(self):
        print("Azul")


semaforo = SemaforoPlus()

semaforo.mudar()
semaforo.mudar()
semaforo.mudar()

semaforo.emergencia()