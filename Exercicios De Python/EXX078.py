lista = []
expressao = input("Digite uma expressão: ")
valida = True
for simbolo in expressao:
    if simbolo == "(":
        lista.append(simbolo)
    elif simbolo == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            valida = False
            break
if len(lista) == 0 and valida:
    print("Expressão válida!")
else:
    print("Expressão inválida!")