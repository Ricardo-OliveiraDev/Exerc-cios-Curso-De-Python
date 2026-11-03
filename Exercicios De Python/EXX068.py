tabela = (
    "Palmeiras",
    "Flamengo",
    "Athletico-PR",
    "Fluminense",
    "Cruzeiro",
    "Bahia",
    "Red Bull Bragantino"
    "Coritiba",
    "Atlético-MG",
    "Corinthians",
    "Botafogo",
    "Vitória",
    "São Paulo",
    "Santos",
    "Grêmio",
    "Internacional",
    "Mirassol",
    "Remo",
    "Vasco",
    "Chapecoense"
    )
print(f"{"Desafio 73":^50}")
print("="*50)
print(f"5 primeiros colocados na tabela: {tabela[0:5]}")
print("-" * 50)
print(f"Zona de rebaixamento: {tabela[-5:]}")
print("-" * 50)
print(f"Tabela em ordem alfabetica:\n{sorted(tabela)}")
print("-" * 50)
print(f"O time da chapecoense está na posição: {tabela.index("Chapecoense")}")