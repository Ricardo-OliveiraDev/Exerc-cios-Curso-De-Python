numero = int(input("Digite um número: "))
divisor = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        divisor += 1
if divisor == 2:
    print("o valor é primo")
else:
    print("o valor não é primo")
    