valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0

c = int(input("Informe o código:  "))
n = float(input("Informe quantas horas você trabalhou este mês:  ")) 


if (n > 50):
    e = (n - 50) * valor_hora_excedente
    salario = (50 * valor_hora) + e
    print("O Salário total é de R$ {0:.2f}".format(salario))
    print("Salário excedente R$ {0:.2f}".format(e))
else:
    salario = (n * valor_hora)
    print("Salário TOtal R$ {0:.2f}".format(salario))
    print("Salário excedente R$ {0:.2f}".format(e)) 