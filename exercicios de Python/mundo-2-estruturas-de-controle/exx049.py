frase = input("Digite uma frase para saber se ela é um palindromo: ").strip().lower()
frase = frase.replace(" ","")
contagem = len(frase)
invertido = ""
for c in range(contagem - 1, -1, -1):
    invertido += frase[c]
if invertido == frase:
    print("É um palindromo!")
else:
    print("Não é um palindromo!")