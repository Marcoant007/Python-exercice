#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
# o mais baixo, a mais gordo e o mais magro, 
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código,
# sua altura e seu peso. 
# O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
# Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto,
# do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
# [Identificar mais alto e magro ou mais baixo e gordo é bônus]. 
#pegar o codigo
#pegar a altura
#pegar o peso
#Informar o mais alto e o codigo
#Informar o mais gordo
#Calcular a media de altura e peso de todos os clientes 

maisAlto = {"codigo": 1, "altura":0, "peso":0}
maisGordo = {"codigo": 1, "altura":0, "peso":0}
alturas = []
pesos = []

codigo = 1
while codigo != 0:
    codigo = int(input("Informe seu código: "))

    if(codigo == 0):
        break

    altura = float(input("Informe sua altura: "))
    peso = float(input("Informe seu peso: "))
    alturas.append(altura)
    pesos.append(peso)

    if(altura > maisAlto["altura"]):
        maisAlto = {"codigo":codigo,"altura":altura,"peso":peso}
        
    if(peso > maisGordo["peso"]):
        maisGordo = {"codigo":codigo,"altura":altura,"peso":peso}

alturaMedia = sum(alturas)/len(alturas)
peso = sum(pesos)/len(pesos)

print("A média entre as alturas é: ", alturaMedia)
print("O mais alto é: ",maisAlto)
print("O mais gordo é: ", maisGordo)
