# Criar lista 1 a 20 
import random

lista = []

random.seed(42)
for c in range(0, 10):
   num = random.randint(1, 20);
   lista.append(num)

# Ordenar lista
lista.sort()

# criar duas listas e dividir
length = len(lista)
middle_index = length//2 ## divide pela metade

first_half = lista[:middle_index] ## com esses : pega a primeira metade da lista
second_half = lista[middle_index:] 

soma_fh = sum(first_half)
soma_sh = sum(second_half)

diferenca = soma_sh - soma_fh

print(f'Lista A : {first_half} com o total de {soma_fh} \n Lista B : {second_half} com o total de {soma_sh}')
print(f'A diferença da soma das listas é: {diferenca}')
# somar o total de cada lista e imprime a diferença 


