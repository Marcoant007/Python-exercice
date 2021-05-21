area = float(input("Informe o tamanho da area em metros?: "))
preco = float(input("Informe o preço por m²: "))

valorFinal = float(area * preco)

print("O valor do carpete será de {0:.2f}".format(valorFinal))