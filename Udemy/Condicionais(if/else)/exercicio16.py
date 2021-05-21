indice = float(input("Informe o indice de poluição: "))


if (indice >= 0.3 and indice < 0.4):
    print("Atenção: Indústrias do 1* grupo devem suspender as atividades.")
elif (indice >= 0.4 and indice < 0.5):
    print("Atenção: Indústrias do 1* e 2* grupo devem suspender as atividades")
elif (indice >= 0.5):
    print("Atençao: Todos os grupos devem suspender as atividades")
else:
    print("Ah você ta de boa")        
