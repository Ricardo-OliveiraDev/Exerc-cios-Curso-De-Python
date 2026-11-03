maior = menor = 0
lista = list()
for c in range(5):
    lista.append(int(input(f"Digite um número na posição {c}: ")))
maior = menor = lista[0]
ind = indmenor = 0
print("=" * 30)
print(f"A lista digitada foi {lista}")
for c, v in enumerate(lista):
    if v > maior:
        maior = v
        ind = c
    if v < menor:
        menor = v
        indmenor = c
print(f"O menor valor foi {menor} e está na posição {indmenor} e o maior foi {maior} na posição {ind}!")