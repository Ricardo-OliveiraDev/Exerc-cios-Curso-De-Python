lista = ("ricardo",
         "alfred",
         "maria",
         "joao", "kleber", "maxuel")
for palavra in (lista):
    print(f"\nna palavra {palavra} temos as vogais: ", end = "")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end = " ")
