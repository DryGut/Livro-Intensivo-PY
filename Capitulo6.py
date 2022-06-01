#Exercicios do Capitulo 6

#exercicios 6.1 a 6.3

dic_nomes = {'nome': 'renato', 'sobrenome': 'martins', 'cidade': 'recife', 'idade': '37'}

for key, value in dic_nomes.items():
  print(key +":"+" "+str(value))

f_num = {'renato': 33, 'marley': 18, 'cal': 15, 'cynthia': 37}

for key, value in f_num.items():
  print("\nO numero favorito de "+ key.title() +" e: "+str(value)+".")


glossario = {'string': 'palavra', 'lower': 'minuscula', 'upper': 'maiuscula'}

for key, value in glossario.items():
  print('\nA '+key+' e uma '+value)

#exercicios 6.4 a 6.6

rios = {'nilo': 'egito', 'eufrates': 'mesopotamia', 'amazonas': 'brasil'}

for key, value in rios.items():
  print('\nO rio '+key.title()+' corta a regiao do(a): '+value.title())

fav_ling = {'renato': 'php', 'marley': 'javascript', 'cal': 'c'}

fav_ling1 = ['joao', 'cynthia', 'ykaro', 'renato', 'cal', 'marley']

for key in fav_ling1:
  if key in fav_ling.keys():
    print("\n"+key.title()+" Obrigado por ter respondido a enquete")
  if key not in fav_ling.keys():
    print("\n"+key.title()+", voce gostaria de responder a enquete?")

#exercicios 6.7 a 6.9

dic_nomes2 = {'nome': 'marley', 'sobrenome': 'martins', 'cidade': 'recife', 'idade': '18'}

dic_nomes3 = {'nome': 'cal', 'sobrenome': 'martins', 'cidade': 'recife', 'idade': '15'}

pessoas = [dic_nomes, dic_nomes2, dic_nomes3]

for pessoa in pessoas:
  for key, value in pessoa.items():
    print("\n"+key.title()+":"+" "+value.title())

alastor = {'gato': 'cal'}
bob = {'cachorro': 'marley'}
pinto = {'passaro': 'cynhtia'}

animais = [alastor, bob, pinto]

for animal in animais:
  for key, value in animal.items():
    print('\nO animal de estimacao e um: '+key+', e seu dono se chama: '+value.title())