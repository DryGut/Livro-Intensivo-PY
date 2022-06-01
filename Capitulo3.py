#exercicios do capitulo 3 'trabalhando LISTAS'

#exercicios 3.1 a 3.3

nomes = ['renato', 'cynthia', 'marley', 'cal']

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

msg = "oi "
msg1 = " como voce esta?"

print("\n"+msg + nomes[0].title() + msg1)
print("\n"+msg + nomes[1].title() + msg1)
print("\n"+msg + nomes[2].title() + msg1)
print("\n"+msg + nomes[3].title() + msg1)

carros = ['honda', 'toyota', 'fiat']

msg2 = "Gostaria de ter um carro da marca: "

print("\n"+msg2 + carros[0].title())
print("\n"+msg2 + carros[1].title())
print("\n"+msg2 + carros[2].title())

#exercicios 3.4 a 3.7

familia = ['cynthia', 'marley', 'cal']

for item in familia:
  print("\nVamos jantar hoje? " + item.title())

print("\nInfelizmente " + familia[0].title() + " nao podera comparecer.")

familia[0] = 'mainha'

for item in familia:
  print("\nVamos jantar hoje? " + item.title())

print("\nAchei uma mesa maior vamos convidar mais gente")

familia.insert(3,"vovo")
familia.insert(4,"painho")
familia.append("cynthia")

for item in familia:
  print("\nVamos iremos jantar nesse restaurante " + item.title() + "\n")

popped_familia = familia.pop(0), familia.pop(4), familia.pop(3), familia.pop(2)
print(popped_familia)

for item in popped_familia:
  print("\nInfelizmente a mesa nao chegou a tempo " + item.title())

for item in familia:
  print("\nVamos so a gente mesmo. " + item.title())

del familia[0]
del familia[0]

print(familia)

#exercicios 3.8 a 3.10

lugares = ['bali', 'aruba', 'japao', 'estonia', 'zimbabuwe']

print(lugares)

print(sorted(lugares))

print(lugares)

len(lugares)