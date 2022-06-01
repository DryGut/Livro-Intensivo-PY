#Exercicios do Capitulo 7

#exercicios 7.1 a 7.3
"""
carro = input("Qual carro desejaria comprar?\n")

print("\nIrei conferir se temos o modelo: "+carro.title())
"""
"""
pessoas = input('Precisam de mesa para quantas pessoas?\n')

if int(pessoas) > 8:
  print('\nVoces terao que aguardar uma mesa desocupar.')
else:
  print('\nOk, senhores temos uma mesa vaga')
"""
"""
numeros = input('informe um numero e direi se e multiplo de dez.\n')
numeros = int(numeros)

if numeros%10 == 0:
  print('o numero e multiplo de 10')
else:
  print('o numero nao e multiplo de 10')
"""
#exercicios 7.4
"""
prompt = '\ninsira o ingrediente da pizza que desejas: '
prompt += '\ndigite "quit" quando finalizar\n'

while True:
  ingredientes = input(prompt)
  if ingredientes == 'quit':
    break
  else:
    print("\n"+ingredientes+" sera adionado a sua pizza")
"""
#exercicio 7.5
"""
while True:
  idade = int(input('qual a sua idade?: '))
  if idade <= 3:
    print('sua entrada e gratuita')
  elif idade <= 12:
    print('seu ingresso custara 10 reais')
  else:
    print('seu ingresso custara 15 reais')
"""
#exercicio 7.8
"""
pedido_sanduiche = ['bauru', 'misto', 'presunto', 'queijo', 'fiambre',]

pedido_feito = []

for sanduiche in pedido_sanduiche:
  if sanduiche == 'bauru':
    print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'misto':
    print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'presunto':
    print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'queijo':
	  print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'fiambre':
	  print('seu sanduiche '+sanduiche+' esta pronto')
  else:
	  print('não temos esse pedido')
  pedido_feito.append(sanduiche)
print('os pedidos feitos sao: ')
for sand in pedido_feito:
	print(sand)
"""
#exercicio 7.9
"""
prompt = 'faca seu pedido: '

pedido_sanduiche = ['pastrami', 'pastrami', 'pastrami', 'bauru', 'misto', 'presunto', 'queijo', 'fiambre',]

pedido_feito = []

print('estamos sem pastrami')

active = True

while active:
    pedido = input(prompt)
    if pedido == 'pastrami':
      pedido_sanduiche.remove(pedido)
      active = False

for sanduiche in pedido_sanduiche:
  if sanduiche == 'bauru':
    print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'misto':
    print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'presunto':
    print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'queijo':
	  print('seu sanduiche '+sanduiche+' esta pronto')
  elif sanduiche == 'fiambre':
	  print('seu sanduiche '+sanduiche+' esta pronto')
  else:
	  print('não temos esse pedido')
  pedido_feito.append(sanduiche)
print(pedido_feito)
print('\nos pedidos feitos sao: ')
for sand in pedido_feito:
	print(sand)
"""
#exercicio 7.10

def ferias(nome, lugar):
  """cria um dicionario para enquete"""
  local = {nome: lugar}
  return local

prompt = 'Qual seu nome?: '

prompt1 = 'Se pudesse visitar um lugar do mundo, para onde voce iria?: '

locais = []
enquete = True

while enquete:
  nome = input(prompt)
  lugar = input(prompt1)
  locais.append(ferias(nome, lugar))
  repetir = input('digite "sair" para finalizar: ')
  if repetir == 'sair':
    enquete = False
for local in locais:
  for key, value in local.items():
    print(key.title() +' respondeu que iria para: '+value.title())