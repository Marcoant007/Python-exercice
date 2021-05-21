#1. Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido 
# e continue pedindo até que o usuário informe um valor válido.

valor1 = int(input("Informe um valor entre 0 e 10: "))


while(valor1 > 10 or valor1 <0):
    print("Nota invalida, a nota deve ser entre 0 e 10 ")
    valor1 = float(input("Informe um valor entre 0 e 10"))

    print("Nota",valor1)
