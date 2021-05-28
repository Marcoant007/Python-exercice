#Faça um programa que leia 5 números e informe o maior número

maior  = -1
for i in range(5):
    num = float(input("Informe um numero: "))
    if(num > maior):
        maior = num
print("Maior valor é igual =", maior)            