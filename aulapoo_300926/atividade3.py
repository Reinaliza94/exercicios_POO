# classe base
class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    def apresentar(self):
        print("Nome: ", self.nome)
        
# chamou o método construtor na classe aluno, por isso não chama "nome automático."
class Aluno(Pessoa):
    def __init__(self, nome, curso):
        super() . __init__(nome)
        self.curso = curso

    def mostrar_curso(self):
        print("Curso: ", self.curso)

# bloco principal
aluno1 = Aluno("João", "TII")
aluno1.apresentar()
aluno1.mostrar_curso()

