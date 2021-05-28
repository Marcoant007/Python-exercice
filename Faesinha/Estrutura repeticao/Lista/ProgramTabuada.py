#Faça uma taboada de qualquer numero que for informado
numero = int(input("Informe um numero para tabuada: "))

for i in range(0, 11):
    result = i * numero
    print(f"{i} x {numero} = {result}")
