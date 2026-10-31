# 3. Crie uma superclasse ‘Calculadora’, com a capacidade de calcular as 4 operações matemáticas por meio de um único método, que recebe por parâmetro valores decimais e um caractere que representa a operação desejada (+ - / *). Essa classe também deve possuir outro método para o cálculo de porcentagem de um número inteiro. Agora crie uma classe que herda dela chamada ‘CalculadoraPro’, com um método adicional para cálculo de potenciação de números inteiros. Ainda, nessa nova classe, você deverá sobrecarregar o método herdado de cálculo de porcentagem para aceitar números decimais.

class Calculadora:
    def calcular (self, n1, n2, operacao):
        if operacao == "+":
            return n1 + n2
        elif operacao == "-":
            return n1 - n2
        elif operacao == "/":
            if n2 != 0:
                return n1 / n2
            else:
                return "Não é possível realizar a operação"
        elif operacao == "*":
            return n1 * n2
        else:
            return "Operação inválida"

    def porcentagem (self, numero, percentual):
        return numero * percentual / 100

class CalculadoraPro(Calculadora):
    def potenciacao (self, base, expoente):
        return base ** expoente
    def porcentagem(self, numero, percentual):
        return numero * percentual / 100

calc = CalculadoraPro()

print("Soma:", calc.calcular(10.5, 5.5, "+"))
print("Subtração:", calc.calcular(10.5, 5.5, "-"))
print("Multiplicação:", calc.calcular(10.5, 5.5, "*"))
print("Divisão:", calc.calcular(10.5, 5.5, "/"))

print("Porcentagem:", calc.porcentagem(200, 10))
print("Potenciação:", calc.potenciacao(2, 3))

print("Porcentagem decimal:", calc.porcentagem(150.5, 12.5))