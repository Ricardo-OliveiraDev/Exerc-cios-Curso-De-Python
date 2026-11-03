nome = input("Digite seu nome: ").lower()
print(f"A letra A aparece {nome.count("a")} vezes")
print(f"A letra A aparece pela primeira vez na posição {nome.find("a")}")
print(f"A letra A aparece pela última vez na posição {nome.rfind("a")}")