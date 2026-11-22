aluno = {}
aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média do aluno: "))
if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"
print(aluno)
#ainda falta exibir a situação do aluno de forma mais clara