lista = list()
for c in range(5):
    numeros = int(input("Digite o valor que deseja por na lista: "))
    if c == 0 or numeros > lista[-1]:
        lista.append(numeros)
        print("O valor foi adicionado no final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                print(f"O valor foi adicionado na posição {pos}")
                break
            pos += 1
print("=-" * 30)
print(f"A lista final ficou assim: {lista}")