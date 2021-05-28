
horasTrabalhas = int(input("Informe quantas horas você trabalhou: "))
horas = 19.50
salario = (horas * horasTrabalhas)
desconto = (25 * salario)/100


if(salario > 2500):
    salarioFinal = (salario - desconto) 
    print("Seu salário teve um desconto, ficou com R$:",salarioFinal , "e o desconto foi de R$:",desconto)
else:
    print("Seu salário não teve desconto, R$:",salario)    