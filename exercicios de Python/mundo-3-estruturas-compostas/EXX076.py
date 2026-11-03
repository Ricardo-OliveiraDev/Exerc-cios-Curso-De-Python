lista = list()
cont = cont5 = 0
while True:
    numero = int(input("Digite um número para ser colocado na lista:"))
    lista.append(numero)
    cont += 1
    if numero == 5:
        cont5 += 1
    sn = input("Deseja continuar [S/N]?: ").strip().lower()
    if sn == "n":
        break
print(f"""A quantidade de números digitados foi {cont}
a lista de com os valores em ordem decrescente foi: {sorted(lista, reverse = True)}""")
if cont5 >= 1:
    print(f"O valor 5 foi digitado essa quantidade de vezes: {cont5}\ne está na lista")
elif cont5 == 0:
    print("O valor 5 não foi digitado e está fora da lista!")