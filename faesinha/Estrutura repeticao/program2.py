#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro 
# e voltando a pedir as informações.

nomeUsuario = input("Informe o nome do usuário: ")
senhaUsuario = input("Informe a senha do usuário: ")


while nomeUsuario == senhaUsuario:
    print("Sua senha não pode ser igual ao seu nome")      
    nomeUsuario = input("Informe seu nome: ")
    senhaUsuario = input("Informe sua senha: ")


print("Cadastrado com sucesso")    