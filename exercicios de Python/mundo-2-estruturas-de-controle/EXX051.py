for c in range(1,6):
    peso = float(input("Digite seu peso: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"Maior peso: {maior}\nMenor peso: {menor}")
