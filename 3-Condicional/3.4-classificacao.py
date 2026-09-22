# Solicitando as informações do usuário
nome = input ("Digite o nome do usuário: ")
idade = float (input("Digite a idade do usuário: "))

# Classificando o usuário
if idade <= 0:
    classe = "Rescem Nascido"

if idade <= 3:
    classe = "Bebê"

if idade <= 10:
    classe = "Criança"

if idade <= 14:
    classe = "Adolescente"

if idade <= 30:
    classe = "Jovem"

if idade <= 64:
    classe = "Adulto"

else:
    classe = "vintage"

print (f"O usuário {nome} está na classe: {classe}")