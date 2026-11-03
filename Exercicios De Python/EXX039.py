lado1 = int(input("Digite o valor do lado 1: "))
lado2 = int(input("Digite o valor do lado 2: "))
lado3 = int(input("digite o valor do lado 3: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("O segmento pode formar um triângulo do tipo: ", end= "")
    if lado1 == lado2 == lado3:
        print("EQUILÁTERO!")
    elif lado1 != lado2 != lado3 != lado1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("O segmento não pode formar um triângulo!")