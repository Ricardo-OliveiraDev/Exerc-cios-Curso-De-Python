from random import choice
al1 = str(input("Digite o nome do 1° aluno?: "))
al2 = str(input("Digite o nome do 2° aluno?: "))
al3 = str(input("Digite o nome do 3° aluno?: "))
al4 = str(input("Digite o nome do 4° aluno?: "))
print(f"O aluno escolhido para ler na frente foi {choice([al1,al2,al3,al4])}")