num = int(input("Digite um número acima de 1000: "))
unidade = num % 10
dezena = num // 10
centena = dezena // 10
milhar = centena // 10
print(f"Unidade: {unidade}\nDezena: {dezena % 10}\ncentena: {centena % 10}\nMilhar: {milhar % 10}")