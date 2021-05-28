Nota1 = float(input("Informe sua primeira nota: "))
Nota2 = float(input("Informe sua segunda nota: "))

media = (Nota1 + Nota2) / 2
print(media)


if(media == 10.0 ):
    print("Aprovado com Distinção")
elif(media >= 7):
    print("Aprovado")
elif(media < 7):
    print("Reprovado")

   
