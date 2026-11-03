from random import randint
maior = menor = 0
tupla = ()
for c in range(5):
    valor = randint(1, 10)
    if c == 0:
        maior = menor = valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor
    tupla += (valor,)
print(tupla, f"""
O maior Número foi :{maior}
E o menor foi: {menor}
Finalizando programa...""")
