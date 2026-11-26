aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média do aluno: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
elif aluno["media"] >= 5:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"
for k, v in aluno.items():
    print(f"{k}: {v}")