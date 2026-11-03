sexo = input("Informe o seu sexo [M/F]: ").lower().strip()
while sexo not in ["m", "f"]:
     print("Digite um Sexo válido!")
     sexo = input("Informe o seu sexo [M/F]: ").lower().strip()
if sexo == "m":
    sexo = "Masculino"
else:
    sexo = "Feminino"
print(f"Sexo Válido Como: {sexo}")