#criando uma classe usuario

class User():
  """inicializa a classe"""
  def __init__(self, name, last):
    self.name = name
    self.last = last
    self.login_attempts = 0

  def describe_user(self):
    """formata o nome quando logado"""
    print(self.name.title() +" "+self.last.title())

  def greet_user(self):
    """sauda o usuario após logado"""
    print("Olá "+ self.name.title() +" "+ self.last.title()+" seja bem vindo")

  def increment_login_attempts(self, login):
    """mostra quantos logins foram feitos"""
    self.login_attempts += login
    print("Voce logou "+str(login)+" vezes")

#criando a classe administrador

class Admin(User):
  """inicializa a classe admin"""

  def __init__(self, name, last):
    """inicializa atributos da classe-pai"""

    super().__init__(name, last)
    self.privileges = Privilege()

#criando a classe privilegios

class Privilege():
  """inicializa a classe privileges"""

  def __init__(self):
    """define os privilegios de admin"""

    self.admin_privileges = admin_privileges = ['can add post', 'can delete post', 'can ban users']

  def show_privileges(self):
    """informa quais privilegios admin tem"""

    for privilege in self.admin_privileges:
      print("Admin can: "+privilege.title())
