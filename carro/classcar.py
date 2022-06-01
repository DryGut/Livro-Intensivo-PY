#criando uma classe carro

class Car():
  """inicializa a classe carro"""
  
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def descriptive_name(self):
    """devolve um nome formatado do carro"""
    
    long_name = str(self.year) +' '+ self.make + ' '+ self.model
    return long_name.title()

  def read_odometer(self):
    """faz a leitura do odometro do carro"""
    
    print("This car has " + str(self.odometer_reading) + " Km on it.")

  def update_odometer(self, mileage):
    """define um valor ao odometro e rejeita alteração"""
    
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You cant roll back an odometer!")

  def increment_odometer(self, miles):
    """incrementa o valor do odometro"""
    
    self.odometer_reading += miles
