soma = 0
for c in range(1, 7):
    par = int(input("Digite um número: "))
    if par % 2 == 0:
        soma += par
print(f"A soma entre os valores é {soma}")