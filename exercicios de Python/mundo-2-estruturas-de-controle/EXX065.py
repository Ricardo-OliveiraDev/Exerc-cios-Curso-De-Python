mulher_menor = homens = maior_de_18 = 0
while True:
    idade = int(input("Quantos anos o Usuário tem ?: "))
    if idade > 18:
        maior_de_18 += 1
    genero = input("Digite o sexo do Usuário [M/F]: ").strip().lower()[0]
    if genero == "m":
        homens += 1
    elif genero == "f" and idade < 20:
        mulher_menor += 1
    resposta = input("Quer continuar: [S/N]").strip().lower()[0]
    if resposta == "n":
        break
    print("-" * 30)
print("-" * 30)
print(f"""LISTA DE CADASTROS:
Pessoas com mais de 18 anos: {maior_de_18}
{"-"*30}
Homens cadastrados: {homens}
{"-"*30}
Mulheres menores de 20 anos: {mulher_menor}
{"-"*30}
Finalizando programa...""")