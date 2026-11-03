viagem = float(input("Digite quantos KM sua viagem tem: "))
if viagem <= 200:
    valor = viagem * 0.50
    print(f"Para fazer a sua viagem de {viagem}KM ela custará R${valor:.2f}!")
else:
    valor = viagem * 0.45
    print(f"Para fazer a sua viagem de {viagem}KM ela custará R${valor:.2f}!")
