nota1 = float(input("Digite o valor da sua primeira nota: "))
nota2 = float(input("Digite o valor da sua segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Você foi \033[4;32mAPROVADO\033[m! PARABÉNS")
elif media < 5:
    print("Você foi \033[4;31mREPROVADO\033[m! Estude mais!")
else:
    print("Você ficou de \033[4;33mRECUPERAÇÃO\033[m! Boa Sorte!")