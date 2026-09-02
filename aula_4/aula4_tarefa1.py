class Livro:
    def __init__(self, titulo, autor, situacao= "Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.situacao = situacao

    def exibir_dados(self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)
        print("Situação: ", self.situacao)

    def exibir_aviso (self, mensagem):
        print("Livro: ", self.titulo)
        print("Aviso: ", mensagem)

livro1 = Livro ("1984", "George Orwell")
livro1.exibir_dados()
livro1.exibir_aviso("Disponível para empréstimo")