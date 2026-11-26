aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média do aluno: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"
print(f"Nome: {aluno['nome']}")
print(f"Média: {aluno['media']}")
print(f"Situação: {aluno['situacao']}")