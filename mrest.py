from classrest import Restaurant

jantar = Restaurant('boi & brasa', 'churrascaria')
jantar.describe_rest()
jantar.open_rest()

atendimento = True
while atendimento:
  at = int(input("Quantidade de pessoas atendidas: "))
  jantar.increment_number_served(at)
  cancelar = input("digite S para sair: ")
  if cancelar == "S":
    atendimento = False
jantar.occupation()