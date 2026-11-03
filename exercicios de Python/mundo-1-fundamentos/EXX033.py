lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("Digite o valor do lado 3: "))
soma_lados = lado1 + lado2
soma_lados1 = lado1 + lado3
soma_lados2 = lado2 + lado3
if soma_lados > lado3 and soma_lados2 < lado1 and soma_lados1 <lado2:
    print(f"OS SEGMENTOS A CIMA PODEM FORMAR UM TRIÂNGULO DO TIPO:",end= "")
    if lado1 == lado2 == lado3:
        print("EQUILÁTERO")
else:
    print(f"NÃO É POSSIVEL FAZER UM TRIANGULO COM OS VALORES LADO: {lado1} LADO: {lado2} LADO: {lado3}")
