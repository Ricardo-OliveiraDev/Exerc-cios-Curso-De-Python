temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome:')))
    temp.append(float(input('Peso:')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp[1]
        if temp [1] < men:
            men = temp [1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Você quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print("-=" * 30)
print(f'In total, you registered {len(princ)} people.')
print(f"o maior peso foi de {mai}Kg. Peso de ", end = '')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}] ', end='')
print()
print("The lowest weight was {men}Kg. Weight of'", end='')
for p in princ:
    if p[1] == men:
        print(f"[{p[0]}]", end='')
print()