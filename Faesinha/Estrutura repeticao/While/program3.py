#3. Faça um programa que leia e valide as seguintes informações:
# 1. Nome: maior que 3 caracteres; (Dica olhar len(nome)) 
# 2. Idade: entre 0 e 150;
# 3. Salário: maior que zero;
# 4. Sexo: 'f' ou 'm';
# 5. Estado Civil: 's', 'c', 'v', 'd';

nome = input("Informe seu nome: ")
while (len(nome) <= 3):
    print("Nome inválido informe novamente")
    nome = input("Informe seu nome: ")
print(nome)

idade = int(input("Informe sua idade: "))
while not 0 < idade < 150:
    print("Idade inválida")
    idade = int(input("Informe sua idade: "))
print(idade)


salario = float(input("Informe seu salário: "))
while salario <= 0:
    print("Salário inválido")
    salario = float(input("Informe seu salário: "))
print(salario)


sexo = input("Informe seu sexo (f) - Feminino ou (m) - Masculino: ")
while (sexo != "f" and sexo != "m"):
    print("Sexo inválido")
    sexo = input("Informe seu sexo (f) - Feminino ou (m) - Masculino: ")
print(sexo)


estadoCivil = input("Informe seu estado civil (s) (c) (v) (d): ")
while "scvd".find(estadoCivil) ==-1:
    print(estadoCivil)
    print("Estado Civil Inválido")
    estadoCivil = input("Informe seu estado civil (s) (c) (v) (d): ")
print(estadoCivil)




