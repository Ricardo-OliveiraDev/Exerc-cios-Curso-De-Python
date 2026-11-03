resposta1 = int(input("Digite um número: ").strip())
resposta2 = int(input("Digite outro número: ").strip())
alternativa = 0
continuar = ""
while alternativa != 5 and continuar != "n":
    print("""O que você deseja fazer com os dois valores digitados?
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]sair""")
    alternativa = int(input("sua resposta: ").strip())
    if alternativa == 1:
        soma = resposta1 + resposta2
        print(f"A soma entre {resposta1} e {resposta2} é :{soma}")
    elif alternativa == 2:
        multiplicar = resposta1 * resposta2
        print(f"A multiplicação de {resposta1} e {resposta2} é :{multiplicar}")
    elif alternativa == 3:
        if resposta1 > resposta2:
            maior = resposta1
        elif resposta2 > resposta1:
            maior = resposta2
        else:
            maior = "Os Valores são iguais!"
        if resposta1 == resposta2:
            print(f"Dentre os valores {resposta1} e {resposta2} não há maior pois {maior}")
        else:
            print(f"Dentre os números {resposta1} e {resposta2} o maior é :{maior}")
    elif alternativa == 4:
        resposta1 = int(input("Digite um número: ").strip())
        resposta2 = int(input("Digite outro número: ").strip())
    elif alternativa == 5:
        print("Finalizando programa...")
    else:
        print("ALTERNATIVA INVÁLIDA! Digite um valor entre 1 e 5!")
    if alternativa != 5 and alternativa in range(1, 6):
        continuar = input("Deseja continuar? [S/N]: ").strip().lower()
        while continuar not in ["s", "n"]:
            print("DIGITE SOMENTE [S/N]!")
            continuar = input("Deseja continuar? [S/N]: ").strip().lower()
        if continuar == "n":
            print("Programa finalizando...")
