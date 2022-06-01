from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phill'] = 'python'

for name, language in favorite_languages.items():
  print(name.title() + "'s favorite language is " + language.title() + ".")

glossario = OrderedDict()

glossario = {'string': 'palavra', 'lower': 'minuscula', 'upper': 'maiuscula'}

for name, type in glossario.items():
  print(name.title() + " it's type is: " + type.title() + ".")
  