#cria uma classe restaurante e registro de atendimento

class Restaurant():
  """inicializa a classe"""
  def __init__(self, rest_name, rest_type):
    self.rest_name = rest_name
    self.rest_type = rest_type
    self.number_served = 0

  def describe_rest(self):
    """informa o nome do restaurante e sua culinaria"""
    print("####### "+self.rest_name.title() +" "+self.rest_type.title()+" #######")

  def open_rest(self):
    """informa que o restaurante se encontra aberto"""
    print("####### "+self.rest_name.title()+" is open #######")

  def set_number_served(self):
    """insere a quantidade de clientes em atendimento"""
    print("We have: " + str(self.number_served) +" people in the house")

  def increment_number_served(self, served):
    """atualiza a quantidade de pessoas em atendimento"""
    self.number_served += served

  def occupation(self):
    """define o limite de ocupacao do restaurante"""
