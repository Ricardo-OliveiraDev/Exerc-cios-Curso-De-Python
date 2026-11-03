peso = float(input("Me diga quantos Kg você pesa: "))
altura = float(input("Agora me diga a sua altura: "))
imc = peso / (altura * altura)
if imc <= 18.4:
    print("Você está \033[4;31mabaixo\033[m do peso! Procure um nutricionista!")
elif imc <= 24.9:
    print("Você está com um peso \033[4;32mnormal\033[m! Parabéns!")
elif imc <= 29.9:
    print("Você está com \033[4;33msobrepeso\033[m! Procure um nutricionista!")
elif imc <= 34.9:
    print("Você está com \033[4;34mObesidade grau 1\033[m! Busque auxílio médico!")
elif imc <= 39.9:
    print("Você está com \033[4;35mObesidade grau 2\033[m! Busque auxílio médico!")
else:
    print("Você está com \033[4;31mObesidade grau 3\033[m! Busque auxílio médico com urgência!")