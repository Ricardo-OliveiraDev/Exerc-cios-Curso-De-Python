primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
contador = 1
limite = 10
resposta = 1
while resposta != 0:
    while contador <= limite:
        print(primeiro,"->", end= " ")
        primeiro = primeiro + razao
        contador += 1
    print("Pausa")
    resposta = int(input("Deseja continuar? digite quantos termos mais quer fazer: "))
    limite += resposta
print("Fim")