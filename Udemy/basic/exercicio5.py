valor_hora = float(input("Quanto você ganha por hora ?: "))
horas_trabalhadas = int(input("Quantas horas você trabalhou neste mês?: "))

salario = (valor_hora * horas_trabalhadas)


print("Esse mês você vai receber R$ {0:.2f}".format(salario))