media = float(input("Informe a média do aluno: "))
aulas = int(input("Quantas aulas tiveram: "))
faltas = int(input("Quantas faltas você teve: "))


presenca = (aulas - faltas) / aulas 


if(presenca < 0.75 ):
    print("Reprovado por falta")
elif (media >= 6):
    print("Aprovado")
else:
    print("Reprovado por nota")    