class Calculadora:
    def dividir (self, numerador, denominador):
        try:
            numerador = int(numerador)
            denominador = int(denominador)

            resultado = numerador / denominador

            print(f"Resultado: {resultado}")
        except ValueError:
            print("Erro: informe apenas numeros inteiros.")
        except ZeroDivisionError:
            print("Erro: nao e possivel dividir por zero.")


#Bloco principal
calculadora1 = Calculadora()
numerador = input("Digite o numerador: ")
denominador = input("Digite o denominador: ")

calculadora1.dividir(numerador, denominador)