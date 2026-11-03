resposta = contador = soma = 0
while resposta != 999:
    resposta = int(input("Digite qualquer número para acumular [Digite 999 para finalizar]: "))
    if resposta == 999:
        print("Finalizando...")
    else:
        soma += resposta
        contador += 1
print(f"Foram digitados {contador} números que somados resultam em: {soma}!")