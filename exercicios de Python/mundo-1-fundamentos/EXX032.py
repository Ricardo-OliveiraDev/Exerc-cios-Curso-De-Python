salario = float(input("Digite seu sálario para calcularmos o seu aumento: R$"))
if salario <= 1250:
    aumento = salario * 0.15
    print(f"Seu sálario saiu de R${salario:.2f} para R${aumento + salario:.2f}")
else:
    aumento = salario * 0.10
    print(f"Seu sálario saiu de R${salario:.2f} para R${aumento + salario:.2f}")
