# Sua organização acaba de contratar um estagiario para trabalhar no suporte, com a intenção de fazer um levantamento
# A primeira tarefa dele é testar todos os cerca de 200 mouses de quecontrar lá, testando e anotando o estado de cada um deles
# Para verificar o que se pode aproveitar deles.
#O programa deverar receber um numero indeterminado de entradas, cada uma contendo: um numero de identificação do mouse e o tipo de defeito
# necessida da esfera
# necessita de limpeza
# necessida de troca do cabo ou conector
# quebrado ou inutilizado
# Ao final devera emitir o seguinte relatório: 
# Quantidade de mouses: 100

#Situação                                   Quantidade      Percentual
#1-necessita da esfera                           40             40%
#2-necessita de limpeza                          30             30%
#3-necessita troca do cabo ou conector           15             15%
#e etc...


contador_total = 0
contador_situacao1 = 0
contador_situacao2 = 0
contador_situacao3 = 0
contador_situacao4 = 0


indetificador = int(input("Informe a identificação: "))

while indetificador != 0:
    print("1- Necessidade de esfera. ")
    print("2- Necessidade de limpeza. ")
    print("3- Necessidade de troca do cabo ou conector. ")
    print("4- Quebrado ou inutilizado. ")
    defeito = int(input("Informe o tipo de defeito: "))
    if (defeito == 1):
        contador_situacao1 = contador_situacao1 +1
    elif(defeito == 2):
        contador_situacao2 = contador_situacao2 +1
    elif(defeito ==3):
        contador_situacao3 = contador_situacao3 +1
    elif(defeito ==4):
        contador_situacao4 = contador_situacao4 +1
    contador_total = contador_total +1
    indetificador = int(input("Informe a identificação: "))
p1 = contador_situacao1 / contador_total * 100.0
p2 = contador_situacao2 / contador_total * 100.0
p3 = contador_situacao3 / contador_total * 100.0
p4 = contador_situacao4 / contador_total * 100.0


print("Situação                                Quantidade  Percentual")
print("1- Necessidade de esfera                    {0}        {1:.2f}%".format(contador_situacao1, p1))
print("2- Necessidade de limpeza                   {0}        {1:.2f}%".format(contador_situacao2, p2))
print("3- Necessidade troca do cabo ou conector    {0}        {1:.2f}%".format(contador_situacao3, p3))
print("4- Quebrado ou inutilizado                  {0}        {1:.2f}%".format(contador_situacao3, p3))



