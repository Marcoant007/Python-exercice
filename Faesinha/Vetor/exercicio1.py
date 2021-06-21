import random

lista = []

random.seed(42)
for c in range(0, 10):
   num = random.randint(0, 99);
   lista.append(num)

lista.sort(reverse=True)

final_list = list(dict.fromkeys(lista))   
print(f'{final_list[1]} é o segundo maior valor')

tamanhoLista = len(final_list)

terceiroElemento = final_list[tamanhoLista -3] 

print(f'{terceiroElemento} é o terceiro menor valor')
