from random import randint

class Dice():
  """inicializa um dado"""

  def __init__(self, sides=6):
    """cria os lados do dado"""
    self.sides = sides

  def roll_dice(self):
    """joga o dado"""
    numbers = randint(1, self.sides)
    print(numbers)

dado = Dice(10)
dado.roll_dice()