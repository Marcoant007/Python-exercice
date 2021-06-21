notaSuperior = 0 

for c in range(0, 10):
    notaC1 = int(input("Informe sua nota na c1: "))
    notaC2 = int(input("Informe sua nota na c2: "))
    media = (notaC1 + notaC2)/2
    print(media)
    if(media > 7.0):
        notaSuperior += 1
      
print(f"{notaSuperior} Alunos Ficaram a cima da média")