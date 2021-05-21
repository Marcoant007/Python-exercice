maior = 0
numero = int(input("Informe um numero: "))


while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input("Informe um número: "))
print("O maior numero é {0}".format(maior))        


#Enquanto o numero for diferente de 0 continua repetindo, se for 0 para o programa