lista = [[],[],[]]
par = 0
for l in range(3):
    for c in range(3):
        num = int(input(f"Digite o número para por na matriz [{l}, {c}]: "))
        if num % 2 == 0:
            par += num
        lista[l].append(num)
print("-=" * 20)
for l in range(3):
    for c in range(3):
        print(f"[{lista[l][c]:^5}]", end= "")
    print()
print("-=" * 20)
print(f"Soma dos valores pares: {par}")
print(f"A soma dos valores da terceira coluna é: {lista[0][2] + lista[1][2] + lista[2][2]}")
maior = lista[1][0]
for c in range(3):
    if lista[1][c] > maior:
        maior = lista[1][c]
print(f"O maior valor da 2 linha foi: {maior}")