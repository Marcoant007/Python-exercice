altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo: (M)Masculino ou (F)Feminino:  ")

if (sexo.lower() == 'm'):
    peso_ideal = (72.7 * altura) - 58
elif (sexo.lower() == 'f'):
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido")
print("Seu peso ideal é {0:.2f}".format(peso_ideal))