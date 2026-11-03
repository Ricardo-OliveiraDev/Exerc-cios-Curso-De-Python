from math import sin, cos, tan, radians
ang = float(input("Qual o valor do ângulo?: "))
conv = radians(ang)
print(f"SENO:{sin(conv):.2f}\nCOSSENO:{cos(conv):.2f}\nTANGENTE:{tan(conv):.2f}")