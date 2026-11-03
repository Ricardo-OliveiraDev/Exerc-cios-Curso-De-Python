extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis",
           "sete", "oito", "nove", "dez", "onze",
           "doze", "treze", "quatorze", "quinze", "dezesseis",
           "dezessete", "dezoito", "dezenove", "vinte")
while True:
    resposta = int(input("Digite um número entre 0 e 20: "))
    while resposta < 0 or resposta > 20:
        resposta = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {extenso[resposta]}")
    continuar = input("deseja continuar? [S/N]: ").lower().strip
    if continuar == "n":
        break