#programa para criação de listas diversas.

def lista(name, last):
  """ gera um dicionario para armazenar os dados """
  data = {name: last}
  return data

to_do = []
insert = True

while insert:
  name = input('insira o nome desejado: ')
  last = input('insira o dado desejado: ')
  to_do.append(lista(name, last))
  repeate = input('digite "SAIR" para finalizar ou tecle ENTER para continuar: ')
  if repeate == 'SAIR':
    insert = False

print(to_do)

for lista in to_do:
  for key, value in lista.items():
    full_name = key+' '+value

    file = 'dados.txt'
    with open(file, 'a') as arq:
      arq.write('\n'+full_name.title())