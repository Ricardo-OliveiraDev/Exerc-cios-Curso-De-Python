valor1  = int(input("Digite o primeiro \033[7;31;40mvalor\033[m:"))
valor2 = int(input("Digite o segundo \033[7;36;40mvalor\033[m: "))
if valor1 > valor2:
    print(f"O valor {valor1} é \033[7;32;40mmaior\033[m do que o valor {valor2}!!")
elif valor2 > valor1:
    print(f"O valor {valor2} é \033[7;34;40mmaior\033[m do que o valor {valor1}!!")
else:
    print(f"O valor {valor1} e o valor {valor2} são \033[7;33;40miguais\033[m!!")