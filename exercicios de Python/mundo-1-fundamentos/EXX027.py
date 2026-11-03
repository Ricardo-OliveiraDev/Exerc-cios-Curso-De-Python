velocidade = int(input("Qual a velocidade que você passou no radar ?:"))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE DE 80 Km/h\nVOCÊ RECEBERÁ UMA MULTA NO VALOR DE R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade de 80 Km/h")