#exercicios do Capitulo 9

#exemplo

class Dog():
  """modelando um cachorro"""
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    """simula um cachorro sentando"""
    print(self.name.title() + ' is now sitting')

  def roll_over(self):
    """simula um cachorro rolando"""
    print(self.name.title() + ' rolled over!')

my_dog = Dog('bob', 13)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

#exercicio 9.1

class Restaurant():
  """cria um restaurante e seus atributos"""
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    """informa o nome e o tipo de cozinha"""
    print("The " + self.restaurant_name.title() + " is a: "
    + self.cuisine_type.title())

  def open_restaurant(self):
    """informa se o restaurante esta aberto"""
    print(self.restaurant_name.title() + " is now open")

jantar = Restaurant("boi & brasa", "churrasco")
print("Hoje iremos jantar no: " + jantar.restaurant_name.title() + "\n")
jantar.open_restaurant()

#exercicio 9.3

class User():
  """inicializa a classe"""
  def __init__(self, name, last, age, born):
    self.name = name
    self.last = last
    self.age = age
    self.born = born

  def describe_user(self):
    print("Your name are: "+self.name.title())
    print("\nYou last name are: "+self.last.title())
    print("\nYour age are: "+str(self.age))
    print("\nYou born at: "+self.born.title())

  def greet_user(self):
    print("Hi, "+self.name.title() +" "+self.last.title() +" glad to see you again")

users = User('renato', 'martins', 37, 'olinda')
users.describe_user()
users.greet_user()