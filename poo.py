
# Tarefa 1.
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

livro = Livro ("O pequeno príncipe", "Antonine de Saint-Exupery", 1943)
print(f"Titulo: {livro.titulo}")
print(f"autor: {livro.autor}")
print(f"ano: {livro.ano}")


#Tarefa 7.

class Terreno:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Area:", self.area)

terreno = Terreno("Terreno 1",0)
largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: ")) 
terreno.area = largura * comprimento
terreno.mostrar_dados()

        
      
    
    

