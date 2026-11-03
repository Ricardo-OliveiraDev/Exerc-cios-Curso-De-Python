mulher_menor = 0
homi = 0
med = 0
nome_homi = ""
for c in range(1,5):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    med += idade
    sexo = input("Digite seu sexo (M/F)").lower().strip()
    if sexo == "f" and idade < 20:
        mulher_menor += 1
    if sexo == "m" and idade > homi:
        homi = idade
        nome_homi = nome
print(f"""O homem mais velho é o {nome_homi} com a idade de {homi} anos
{mulher_menor} Mulheres tem menos de 20 anos
E a média de idade do grupo é {med /4:.1f}""")
