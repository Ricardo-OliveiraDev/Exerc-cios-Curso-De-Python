turma = []
while True:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input(f"Digite a 1ª nota de {nome}: "))
    nota2 = float(input(f"Digite a 2ª nota de {nome}: "))
    media = (nota1 + nota2) / 2
    turma.append([nome, [nota1, nota2], media])
    continuar = input("Deseja continuar? [S/N] ").strip().lower()
    while continuar not in ("s", "n"):
        continuar = input("DIGITE UMA RESPOSTA VÁLIDA ENTRE S E N! Deseja continuar? [S/N]: ").strip().lower()
    if continuar == "n":
        break
print("-=" * 30)
print("Nº   NOME            MÉDIA")
print("-" * 30)
for indice, aluno in enumerate(turma):
    print(f"{indice:<4} {aluno[0]:<15} {aluno[2]:>5.1f}")
print("-" * 30)
continuar = input("Deseja ver a nota de algum aluno? [S/N] ").strip().lower()
while continuar not in ("s", "n"):
    continuar = input("DIGITE UMA RESPOSTA VÁLIDA ENTRE S E N! Deseja ver a nota de algum aluno? [S/N]: ").strip().lower()
if continuar == "s":
    while True:
        aluno_numero = int(input("Digite o número do aluno que deseja ver as notas (999 para sair): "))
        while aluno_numero not in range(len(turma)) and aluno_numero != 999:
            aluno_numero = int(input("Número de aluno inválido. Digite novamente (999 para sair): ").strip())
        if aluno_numero == 999:
            break
        aluno = turma[aluno_numero]
        print(f"Aluno {aluno[0]} teve as notas: {aluno[1][0]} e {aluno[1][1]}")
            