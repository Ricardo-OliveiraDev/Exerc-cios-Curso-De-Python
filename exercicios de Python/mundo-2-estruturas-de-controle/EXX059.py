resposta = int(input("Digite o número para começar a sequência de fibonacci: "))
contador = 0
n1 = 0
n2 = 1
while contador < resposta:
    print(n1,"->", end=" ")
    soma = n1 + n2
    n1 = n2
    n2 = soma
    contador += 1
print("Fim")