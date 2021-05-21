nota1 = float(input("Informe a nota da primeira prova: "))
nota2 = float(input("Informe a nota da segunda prova: "))
nota3 = float(input("Informe a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

if(media >= 7):
    print(f"Sua média foi de: {media}, portanto esta Aprovado")
elif(media > 5 and media < 7):
    print(f"Sua média foi de: {media}, portanto esta de Recuperação")
elif(media < 5):
    print(f"Sua média foi de: {media}, portanto Reprovado")
else:
    print("Média inválida")            