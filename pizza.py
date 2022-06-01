#prepara uma pizza

def make_pizza(size, *toppings):
  """apresenta pizza que esta preste a ser preparada"""
  
  print("\nMaking a " + str(size) +
  "-inch pizza with the following toppings:")
  for topping in toppings:
    print("- " + topping)