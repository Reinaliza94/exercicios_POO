class Votacao:
  def __init__(self, nome1, nome2, nome3, nome4):
    self.nome1 = nome1
    self.nome2 = nome2
    self.nome3 = nome3
    self.nome4 = nome4

    self.votos1 = 0
    self.votos2 = 0
    self.votos3 = 0
    self.votos4 = 0

 
  def receber_voto(self, numero):
    if numero == 11:
      self.votos1 = self.votos1 + 1
    elif numero == 22:
      self.votos2 = self.votos2 + 1
    elif numero == 33:
      self.votos3 = self.votos3 + 1
    elif numero == 44:
      self.votos4 = self.votos4 + 1
    else:
      print("Número inválido!")

  def retornar_ganhador(self):
    maior_votos = self.votos1
    ganhador = self.nome1

    if self.votos2 > maior_votos:
      maior_votos = self.votos2
      ganhador = self.nome2

    if self.votos3 > maior_votos:
      maior_votos = self.votos3
      ganhador = self.nome3

    if self.votos4 > maior_votos:
      maior_votos = self.votos4
      ganhador = self.nome4

    if maior_votos == 0:
      print("Nenhum voto computado ainda.")

    return ganhador



    
eleicao = Votacao("Candidato A", "Candidato B", "Candidato C", "Candidato D")

print("COMPUTANDO VOTOS")
eleicao.receber_voto(11)  # Voto para Candidato A
eleicao.receber_voto(22)  # Voto para Candidato B
eleicao.receber_voto(22)  # Voto para Candidato B
eleicao.receber_voto(99)  # Voto inválido

  
print("RESULTADO")
vencedor = eleicao.retornar_ganhador()
print(f"O ganhador atual é: {vencedor}")



