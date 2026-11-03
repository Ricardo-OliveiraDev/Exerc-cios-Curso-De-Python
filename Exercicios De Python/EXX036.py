ano = int(input("Digite o seu ano de nascimento: "))
maior_idade = 2026 - 18
if ano <= maior_idade:
    exercito = input("Você já se alistou no exército?:").strip().lower()
    if exercito == "s" or exercito == "sim":
        print("Então está tudo bem, boa sorte no recrutamento!")
    elif exercito == "n" or exercito== "nao" or exercito == "não":
        print("você precisa fazer seu alistamento o mais breve possível!")
    else:
        print("ERRO: Digite apenas [S/N]!")
else:
    print(f"""Já que você nasceu no ano de {ano} você ainda é menor de idade então
só terá que fazer seu alistamento Quando completar 18 anos!!""")
