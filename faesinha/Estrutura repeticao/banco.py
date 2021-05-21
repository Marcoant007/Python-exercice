#Em um banco, as contas são identificadas por um número de conta com dígito verificados. 
#Esse dígito é calculado pelo seguinte modo: Somar todos os dígitos do número da conta, 
#depois dividis a soma por 10 e tomar o resto.
#Exemplo 5713 temos: 5+7+1+3 = 16 dividido por 10 o resto é 6


contador = 0
soma = 0
digitos = 4
while(contador < digitos):
    numero = int(input("Digite o número da conta: "))
    soma = soma + numero
    contador += 1

print("o resultado é ")
print(soma % 10)
