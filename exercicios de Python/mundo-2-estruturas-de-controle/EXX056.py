numero = int(input("Digite um número para te mostrar o fatorial: "))
contador = numero
fatorial = 1
while contador > 1:
    fatorial *= contador
    contador -= 1
print(f"{numero}! = {fatorial}")