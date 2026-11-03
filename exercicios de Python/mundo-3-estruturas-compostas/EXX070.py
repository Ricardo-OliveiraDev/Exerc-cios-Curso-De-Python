tupla = ()
for c in range(4):
    numero = int(input(f"Digite o {c + 1} número: "))
    tupla += (numero,)
print(tupla)
if 9 in tupla:
    print(f"O número 9 apareceu essa quantidade de vezes: {tupla.count(9)}")
else:
    print("O número 9 não foi digitado pelo usuário!")
if 3 in tupla:
    print(f"O número 3 apareceu na posição: {tupla.index(3)+1}")
else:
    print("O número 3 não foi digitado pelo usuário!")
print("Esses foram os números pares: ", end = "")
for c in range(4):
    if tupla[c] % 2 ==  0:
        print(tupla[c], end = " ")
