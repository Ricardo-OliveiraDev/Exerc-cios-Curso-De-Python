media = contador = numeros = maior = menor = 0
resposta = "s"
while resposta == "s":
    numeros = int(input("Digite o numero: ").strip()[0])
    if contador == 0:
        maior = numeros
        menor = numeros
    if numeros > maior:
        maior = numeros
    elif numeros < menor:
        menor = numeros
    media += numeros
    contador += 1
    resposta = input("Deseja continuar? [S/N]: ").lower().strip()
print(f"A média entre todos eles foi {media / contador} o maior foi {maior} e o menor foi {menor}!")