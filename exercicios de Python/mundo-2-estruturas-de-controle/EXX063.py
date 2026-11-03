c = 0
while True:
    tabuada = int(input("digite um número para mostrar a tabuada[Digite numero negativo para sair]: "))
    if tabuada < 0:
        break
    while True:
        if c >=10:
            break
        c += 1
        print(f"{tabuada} x {c} = {tabuada*c}")
        print(f"{"-":-^12}")
    c = 0
print("Programa finalizando...")