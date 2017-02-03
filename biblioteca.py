def gera_nome_convite(nome):
  parte1 = nome[0:4]
  parte2 = nome[len(nome)-4:len(nome)]
  return parte1 + ' ' + parte2

def envia_convite(nome):
	print('Enviado convite para '+nome)

def processa_convite(nome):
	envia_convite(gera_nome_convite(nome))
