casa = float(input("Digite o valor da casa: "))
salario = float(input("digite o valor do seu salario: "))
anos = int(input("digite em quantos anos você vai pagar a casa: "))
parcela = (casa / anos) / 12
trinta = salario * 0.30
if parcela > trinta:
    print(f"\033[4;31mNEGADO\033[m! Com o sálario de R${salario} não é possível pagar a parcela de R${parcela:.2f} pois ultrapassa o valor máximo de 30% do seu sálario")
else:
    print(f"PARABÉNS CONTRATO FEITO COM \033[4;32mSUCESSO\033[m!!")