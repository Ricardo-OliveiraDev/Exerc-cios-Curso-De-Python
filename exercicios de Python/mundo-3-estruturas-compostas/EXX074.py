resposta = ""
lista = list()
while "n" not in resposta:
    numero = int(input("Digite um valor: "))
    if numero in lista:
        print("Não irei adicionar o valor pois já tem na lista!")
    else:
        lista.append(numero)
        print("Valor adicionado com sucesso!")
    resposta = input("Deseja continuar? [S/N]: ").lower().strip()
    while resposta not in ("s","n"):
        resposta = input("DIGITE UMA RESPOSTA VÁLIDA ENTRE [S/N]: ")
print("=-" * 30)
lista.sort()
print(f"Os valores digitados foram {lista}")