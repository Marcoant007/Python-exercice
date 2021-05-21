#Desenvolva um gerador de tabuada, capaz de gerar a tabuada 
#de qualquer número inteiro entre 1 a 10. O usuário deve informar qual numero ele deseja ver a tabuada.
#A saida deve ser : 
# Tabuada de 5:
#5x1 = 5, 5x2 = 10, 5x3 = 15, 5x4 = 20;

numero = int(input("Informe um número entre 1 e 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Informe um número entre 1 e 10"))
print("Tabuada de {0}".format(numero))
for n in range(1, 11):
    print("{0} x {1} = {2}".format(numero, n, (numero * n)))
