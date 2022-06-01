#exercicios do Capitulo 8 do livro

#exercicio 8.3
"""
def estampa(tamanho):
  if tamanho == 'P':
    print('sou engraçado')
  elif tamanho == 'M':
    print('tudo nosso')
  elif tamanho == 'G':
    print('e nois')

print(estampa('P'))
print(estampa('M'))
print(estampa('G'))
"""

#exercico 8.4
"""
def estampa(tamanho="G", frase="Eu amo Python"):
  print(tamanho +" "+ frase)

estampa()
estampa('M')
estampa("P", 'python eh massa')
"""
#exercicio 8.5
"""
def descri_cidades(cidade, pais="brasil"):
  print(cidade.title() +' esta localizada no '+ pais.title())

descri_cidades('recife')
descri_cidades('natal')
descri_cidades('nova iorque', 'usa')
"""

#exercicio 8.9 a 8.11


"""
def show_magicians():
  for magician in magicians:
    print(magician)

show_magicians()
"""
"""
def show_magicians(nomes):
    print(nomes)


def make_great(nomes, nomesmod):
    while nomes:
        magico_atual = 'O grande ' + nomes.pop()
        nomesmod.append(magico_atual)
        print(magico_atual)


magicos = ['1', '2', '3', '4']
magicos_grande = []

make_great(magicos, magicos_grande)
show_magicians(magicos)
"""
#exercicios 8.12
"""
def make_sand(*toppings):
  print('Fazendo seu sanduiche com: ')
  for topping in toppings:
    print('- '+topping)

make_sand('atum')
make_sand('atum', 'queijo')
make_sand('atum', 'queijo', 'presunto')
"""
#exercicio 8.13
"""
def build_profile(name, last, **user_info):
  profile = {}
  profile['name'] = name
  profile['lastname'] = last
  for key, value in user_info.items():
    profile[key] = value
    return profile

user = build_profile('renato', 'martins', idade=37, profissao='analista')
print(user)
"""
#exercicio 8.15

