#Exercicios do Capitulo 4 "Listas e laço for"

#exercicios 4.1 e 4.2

pizzas = ['pepperoni', 'mussarela', 'camarao']

for pizza in pizzas:
  print("\nGosto de pizza de: "+pizza.title())

print("\nEu gosto de pizza "+pizzas[0].title() + "\nde pizza de "+pizzas[1].title()+" \ne de pizza de "+pizzas[2].title()+" \nEu gosto muito de pizzas!")

animais = ['gato','tigre', 'pantera', 'puma', 'onca', 'leopardo']

for animal in animais:
  print("\n"+animal.title()+" e um bom cacador.")
print("\nTodos eles sao felinos")

#exercicos 4.6 a 4.9

for i in range(1,21):
  print(i)

impares = list(range(1,21,2))
for i in impares:
  print(i)

tres = []
for valor in range(1,11):
  tres.append(valor*3)
print(tres)

cubos = []
for cubo in range(1,11):
  cubos.append(cubo**3)
print(cubos)

#exercicios 4.10 a 4.12

print("\nOs primeiros animais sao: ")
for animal in animais[:3]:
  print(animal.title())

print("\nOs dois animais do meio sao: ")
for animal in animais[2:4]:
  print(animal.title())

print("\nOs ultimos animais sao: ")
for animal in animais[3:]:
  print(animal.title())

Apizzas = pizzas[:]

pizzas.append("calabresa")
Apizzas.append("portuguesa")
print(pizzas)
print(Apizzas)
print("\nMinhas pizza favoritas sao: ")
for item in pizzas:
  print(item.title())

print("\nAs pizzas favoritas dos meus amigos sao: ")
for item in Apizzas:
  print(item.title())
print("\n")
#exercicios 4.13

pratos = ('lasanha', 'arrumadinho', 'feijoada', 'dobradinha', 'sarapatel')

for prato in pratos:
  print(prato)

pratos = ('lasanha', 'sarapatel', 'feijoada')

print('\nO novo menu e: ')
for prato in pratos:
  print(prato)