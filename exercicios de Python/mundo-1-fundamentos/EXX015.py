from math import hypot
adj = float(input("Digite o valor do lado adjacente: "))
opo = float(input("Digite o valor do lado oposto do triângulo: "))
print(f"A hipotenusa do triângulo é {hypot(adj, opo):.2f}")