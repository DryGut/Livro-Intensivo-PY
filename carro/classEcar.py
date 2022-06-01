#cria a classe carro eletrico
from classcar import Car


class ElectricCar(Car):
  """representa aspectos especificos de carros eletricos."""
  
  def __init__(self, make, model, year):
    """inicializa atributos da classe-pai"""

    super().__init__(make, model, year)
    self.battery = Battery()

class Battery():
  """inicializa a classe"""

  def __init__(self, battery_size=70):
    """inicializa os atributos da bateria"""

    self.battery_size = battery_size

  def describe_battery(self):
    """exibe a capacidade da bateria"""

    print("This car has a "+ str(self.battery_size)+ "-Kwh battery")

  def get_range(self):
    """exibe a distancia que a bateria suporta"""

    if self.battery_size == 70:
      range = 240
    elif self.battery_size == 85:
      range = 270

    msg = "This car can go approximately "+ str(range) + " Km on full charge."
    print(msg)

