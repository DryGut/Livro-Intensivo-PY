#trabalhando com arquivos JSON

import json
"""
numbers = [2, 3, 4, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as arq:
  json.dump(numbers, arq)

#lendo o arquivo

with open(filename) as arq:
  numbers = json.load(arq)
  print(numbers)
"""

#armazenando entrada de usuarios
"""
username = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as arq:
  json.dump(username, arq)
  print("We'll remember you when you come back, " +username.title()+ "!")
"""
#lendo a entrada de usuarios
"""
filename = 'username.json'

with open(filename) as arq:
  username = json.load(arq)
  print("Welcome back, " +username.title()+"!")
"""

filename = 'username.json'

try:
  with open(filename) as arq:
    username = json.load(arq)

except FileNotFoundError:
  username = input("What is your name? ")
  with open(filename, 'w') as arq:
    json.dump(username, arq)
    print("We'll remember you when you come back, "+username.title()+"!")

else:
  print("Welcome back, "+username.title()+"!")
  