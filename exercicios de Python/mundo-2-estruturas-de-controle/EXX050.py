from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    usuarios = int(input("Digite o seu ano de nascimento:"))
    teste = date.today().year - usuarios
    if teste >= 21:
        maiores += 1
    else:
        menores += 1
print(f"{maiores} usuários são maiores de idade!\n{menores} são menores de idade!")
