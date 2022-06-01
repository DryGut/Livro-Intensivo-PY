#Exercicios Capitulo 5 If statement

#exercicios 5.1 a 5.2

bike = 'caloi'
cor = 'azul'
print("bike == 'caloi'? acho que True.")
print(bike == 'caloi')

print("\nbike == 'trek'? acho que False.")
print(bike == 'trek')

print("\nCor igual a verde?")
print(cor == 'verde')
print("\nCor igual a azul?")
print(cor == 'azul')

itens = ['pedra', 'papel', 'tesoura']
outros = 'cola'
if outros not in itens:
  print(outros+" nao esta na lista")

num = 5

print("5 e menor que 6?")
print(5 == 6)

#exercicios 5.3 a 5.7

alien_cor = 'vermelho'

if alien_cor == 'verde':
  print("\nvoce ganhou 5 pontos")

if alien_cor == 'vermelho':
  print("\nvoce ganhou 5 pontos")

if alien_cor == 'amarelo':
  print("\nvoce ganhou 15 pontos")
else:
  print("\nvoce ganhou 5 pontos")

if alien_cor != 'amarelo':
  print("\nvoce ganhou 15 pontos")
else:
  print("\nvoce ganhou 5 pontos")

if alien_cor == 'verde':
  print("\nvoce ganhou 5 pontos")
elif alien_cor == 'vermelho':
  print("\nvoce ganhou 15 pontos")
elif alien_cor == 'amarelo':
  print("\nvoce ganhou 10 pontos")
else:
  print("\nTente outra vez")

idade = 66
if idade <= 3:
  print("\nvoce e uma criança")
elif idade <= 12:
  print("\nvoce e um garoto")
elif idade <= 19:
  print("\nvoce e um adolescente")
elif idade <= 64:
  print("\nvoce e um adulto")
else:
  print("\nvoce e um idoso")

frutas_favoritas = ['banana', 'laranja', 'uva']

for fruta in frutas_favoritas:
  if fruta == 'banana':
    print('\nvoce realmente gosta de: '+fruta.title())
  elif fruta == 'uva':
    print('\nvoce realmente gosta de: '+fruta.title())
  elif fruta == 'laranja':
    print('\nvoce realmente gosta de: '+fruta.title())

#exercicio 5.8 a 5.11

users = ['Renato', 'marley', 'cal', 'cynthia', 'admin', 'mainha', 'painho']

for user in users:
  if user == 'admin':
    print("\nOla, "+user.title()+" gostaria de ver um relatório de status?")
  else:
    print("\nOla, "+user.title()+" obrigado por fazer o login novamente.")

usuarios = []
if usuarios:
  for usuario in usuarios:
    print("\nVoce esta logado como: "+usuarios.title())
else:
  print("\nPrecisamos encontrar alguns usuarios!")

new_users = ['renato', 'marley', 'joao', 'herbert', 'ykaro']

for user in new_users:
  if user in users:
    print("\nEste nome ja esta sendo usado.")
  else:
    print("\nNome de usuario disponivel.")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for numero in numeros:
  if numero == 1:
    print(str(numero)+"st")
  elif numero == 2:
    print(str(numero)+"nd")
  elif numero == 3:
    print(str(numero)+"rd")
  else:
    print(str(numero)+"th")

