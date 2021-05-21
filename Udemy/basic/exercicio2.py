#entradas
quantidade_minima = int(input("Informe a quantidade minima:  "))
quantidade_maxima = int(input("Informe a quantidade maxima:  "))

estoque_medio = (quantidade_minima + quantidade_maxima) / 2 

print("O estoque médio é {0}".format(estoque_medio))