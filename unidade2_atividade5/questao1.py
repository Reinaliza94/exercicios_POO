class Contador:
    contador = 0

    def aumentar():
        Contador.contador +=1

    def diminuir():
        Contador.contador -=1

    def zerar():
        Contador.contador = 0

    def mostrar():
        print(f"Contador: {Contador.contador}")

