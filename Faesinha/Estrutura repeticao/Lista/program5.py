lim_inf = int(input("Limite inferior"))
lim_sup = int(input("Limite superior"))

soma = 0

for i in range(lim_inf, lim_sup +1):
    print(i, end=" ")
    soma +=i

print("Soma ", soma)