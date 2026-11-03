geral = list()
impar = list()
par = list()
while True:
    num = int(input("Digite um valor para ser acionado a lista:"))
    geral.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    res = input("Deseja continuar? [S/N]: ").lower().strip()
    while res not in ("s", "n"):
        res = input("DIGITE UMA RESPOTA VALIDA!!!\nDeseja continuar? [S/N]: ").lower().strip()
    if res == "n":
        break
print(f"""A lista geral foi: {geral}
A lista impar foi: {impar}
A lista par foi: {par}""")