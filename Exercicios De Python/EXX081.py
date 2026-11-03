lista = [[],[],[]]
for linha in range(3):
    for coluna in range(3):
        num = int(input(f"Digite um valor para a [{linha}, {coluna}]: "))
        lista[linha].append(num)
print("=-" * 20)
for linha in range(3):
    for coluna in range(3):
        print(f"[{lista[linha][coluna]:^5}]", end="")
    print() 