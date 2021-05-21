#Faça um programa que leia um nome de usuário e a sua e não aceite a senha igual o nome do usuário, mostrando a mensagem de  erro
#E voltando a pedir os dados


nome = input("Informe seu nome: ")
senha = input("Informe sua senha: ")


while nome == senha:
    print("Sua senha não pode ser igual ao seu nome")      
    nome = input("Informe seu nome: ")
    senha = input("Informe sua senha: ")


print("Cadastrado com sucesso")    