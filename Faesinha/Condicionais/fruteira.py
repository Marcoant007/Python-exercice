Kgmorango = float(input(("informe quantos Kg de morango vai levar: ")))
Kgmaca = float(input(("informe quantos Kg de mançã vai levar: ")))


preco_maca = Kgmaca * 1.8
preco_morango = Kgmorango * 2.5

if(Kgmorango > 5):
    preco_morango = Kgmorango * 2.2
else:
    preco_morango = Kgmorango * 2.5    

if(Kgmaca > 5):
    preco_maca = Kgmaca * 1.50
else:
    preco_maca = Kgmaca * 1.80    


preco_total = preco_maca + preco_morango

if(Kgmaca + Kgmorango > 8 or preco_total > 25):
    preco_total = preco_total * 0.9
    print("Voce tem um desconto de 10%")


print("Total")
print(f"Maça: {Kgmaca} kgs - Total R${preco_maca:8.2f}")
print(f"Morango: {Kgmorango} kgs - Total R${preco_morango:8.2f}")
print(f"Total: {Kgmaca+Kgmorango:8.2f} kg R${preco_total}")

#pysimpleGUI
#kivy