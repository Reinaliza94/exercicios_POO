# QUESTÃO 8

class Pedido:
    def __init__(self, produto, preco_unitario, quantidade=1):
        self.produto = produto
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.situacao = "Aberto"

    def mostrar_dados(self):
        print("Produto: ", self.produto)
        print("Preço Unitário: ", self.preco_unitario)
        print("Quantidade: ", self.quantidade)
        print("Situação: ", self.situacao)

    def calcular_total(self):
        return self.preco_unitario * self.quantidade

    def alterar_quantidade(self, nova_quantidade):
        self.quantidade = nova_quantidade

p1 = Pedido ("Caderno", 20)
p1.mostrar_dados()
total1 = p1.calcular_total()
print(f"Total: {total1}" )
p1.alterar_quantidade(3)
p1.mostrar_dados()
total1 = p1.calcular_total()
print(f"Total: {total1}")

        
        