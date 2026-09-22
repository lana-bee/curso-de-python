# Solicitando o nome e a idade do usuário
nome = input ("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Criando a condição caso for >= a 18 anos
if idade >= 18:
    print ("Você é maior de idade!")

else:
    print ("Você é menor de idade!")