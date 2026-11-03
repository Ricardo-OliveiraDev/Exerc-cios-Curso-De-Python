c = s = 0
while True:
    n = int(input("Digite um valor [999 para parar]: ").strip())
    if n == 999:
        break
    c += 1
    s += n
print(f"a quantidade de números digitados foi de {c} e a soma deles foi de {s}")