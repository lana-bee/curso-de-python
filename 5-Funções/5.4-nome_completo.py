# Criando a função nome completo
def nome_completo (nome,sobrenome):
    return f"{nome} {sobrenome}" 

# Solicitando o nome e sobrenome do usuário
name = input ("Digite seu nome: ")
surname = input ("Digite seu sobrenome: ")

# Chamando a função e criando o nome inteiro
nome_inteiro = nome_completo (name, surname)

# Apresentando a mensagem de boas vindas ao usuário
print (f"Seja bem-vindo(a) {nome_inteiro}!")
