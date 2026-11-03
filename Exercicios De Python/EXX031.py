n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite o último número: "))
if n1 > n2:
    maior = n1
else:
    maior = n2
if n3 > maior:
    maior = n3
if n1 < n2:
    menor = n1
else:
    menor = n2
if n3 < menor:
    menor = n3
print(f"Dos números que você digitou o maior foi {maior} e o menor foi {menor}!")
