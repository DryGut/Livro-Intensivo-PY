#cria perfil de usuários 

def build_profile(name, last, **user_info):
  profile = {}
  profile['name'] = name
  profile['lastname'] = last
  for key, value in user_info.items():
    profile[key] = value
    return profile

enquete = True

prompt = 'Digite seu nome: '
prompt1 = 'Digite seu sobrenome: '

while enquete:
  name = input(prompt)
  last = input(prompt1)
  a
  
  