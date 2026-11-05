turma = []
while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input(f"Digite a 1ª nota de {nome}: "))
    nota2 = float(input(f"Digite a 2ª nota de {nome}: "))
    media = (nota1 + nota2) / 2
    turma.append([nome, [nota1, nota2], media])
    continuar = input("Deseja continuar? [S/N] ").strip().lower()
    if continuar == 'n':
        break
