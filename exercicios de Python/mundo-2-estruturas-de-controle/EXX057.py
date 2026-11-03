primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
while contador <= 10:
    print(primeiro,"->", end= ' ')
    primeiro = primeiro + razao
    contador += 1
print("Fim")