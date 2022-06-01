#exercicos do Capitulo 10

#exercicio 10.1


#abre o arquivo e le
"""
with open('learning_python.txt') as arquivo:
  contents = arquivo.read()
  print(contents)
"""

#abre o arquivo por linhas e tira a quebra de linhas
"""
filename = 'learning_python.txt'
with open(filename) as arquivo:
  for line in arquivo:
    print(line.rstrip())
"""

#cria uma lista para ser trabalhada fora do bloco with
"""
filename = 'learning_python.txt'
with open(filename) as arquivo:
  lines = arquivo.readlines()
  for line in lines:
    print(line.rstrip())

print(lines)
"""

#exercico 10.2
"""
filename = 'learning_python.txt'
with open(filename) as arquivo:
  for line in arquivo:
    print(line.replace('python', 'c'))
"""

#calculadora simples
"""
print("##### Give me two numbers, to be divide #####")
print("Enter 'q' to quit.")

while True:
  first_number = input("\nfirst number: ")
  if first_number == 'q':
    break
  second_number = input("\nsecond number: ")
  if second_number == 'q':
    break
  try:
    answer = int(first_number) / int(second_number)
  except ZeroDivisionError:
    print("You cant divide by 0!")
  else:
    print(answer)
"""
#tratando erros para arquivos e analisando arquivos
"""
filename = 'ulisses.txt'
try:
  with open(filename) as arq:
    contents = arq.read()
except FileNotFoundError:
  msg = "Sorry, the file "+ filename + " does not exist."
  print(msg)
else:
  words = contents.split()
  num_words = len(words)
  print("The file "+ filename +" has about "+ str(num_words) +" words.")
"""
#tratando erros exercicio 10.6
"""
print("Forneca os numeros")

while True:
  
  num1 = input("first number: ")
  if num1 == 'q':
    break
  
  num2 = input("second number: ")
  if num2 == 'q':
    break
  
  try:
    answer = int(num1) + int(num2)
  
  except ValueError:
    print("can only use number as input")
  
  else:
    print(answer)
"""
