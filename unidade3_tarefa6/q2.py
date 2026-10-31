# 2. Crie uma superclasse chamada ‘Semáforo’, com o método ‘mudar’, que altera a cor da luz seguindo a sequência verde -> vermelho -> amarelo, retomando ao início da sequência. Mas é preciso agora de uma classe ‘SemaforoPlus’, que possui o método ‘emergência’,  que mostra a cor azul, em caso de defeito. Nessa classe, ao chamar o método ‘mudar’, ele deve voltar a realizar a sequência normalmente a partir do início.

class Semaforo:
    def __init__(self):
        self.cor_atual = "Verde"

    def mudar(self):
        if self.cor_atual == "Verde":
            self.cor_atual = "Vermelho"

        elif self.cor_atual == "Vermelho":
            self.cor_atual = "Amarelo"

        elif self.cor_atual == "Amarelo":
            self.cor_atual = "Verde"

        print(self.cor_atual)


class SemaforoPlus(Semaforo):
    def emergencia(self):
        print("Azul")

    def mudar(self):
        self.cor_atual = "Verde"
        super().mudar()

semaforo = Semaforo()
semaforo_plus = SemaforoPlus()

semaforo.mudar()
semaforo.mudar()
semaforo.mudar()

semaforo_plus.emergencia()
semaforo_plus.mudar()