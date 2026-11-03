from random import shuffle
n1 = str(input("Digite o nome do 1° aluno: "))
n2 = str(input("Digite o nome do 2° aluno: "))
n3 = str(input("Digite o nome do 3° aluno: "))
n4 = str(input("Digite o nome do 4° aluno: "))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f"a ordem de apresentação é\n{lista}")