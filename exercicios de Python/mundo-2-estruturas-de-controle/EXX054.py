from random import randint
contador = 1
resposta = int(input("Vamos brincar de adivinhar em qual número estou pensando de 1 a 10! Digite sua resposta: ").strip())
while resposta not in range(1, 11) :
    print("ERRO! Digite um valor válido entre 1 e 10!")
    resposta = int(input("Em que número estou pensando de 1 a 10? Resposta:").strip())
computador = randint(1, 10)
while resposta != computador:
    print("Você errou! tente novamente!")
    resposta = int(input("Em que número estou pensando de 1 a 10? Resposta:").strip())
    while resposta not in range(1, 11):
        print("ERRO! Digite um valor válido entre 1 e 10!")
        resposta = int(input("Em que número estou pensando de 1 a 10? Resposta:").strip())
    contador += 1
print(f"Parabéns você acertou! Pensei no número {computador} mesmo! Você tentou {contador} vezes!")