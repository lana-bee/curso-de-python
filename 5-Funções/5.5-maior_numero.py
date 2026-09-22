# Criando função maior_numero
def maior_numero (a,b):
    if a > b:
        return a
    else: 
        return b
# Solicitando 2 números para o usuário
numero_1 = float(input ("Digite um número: "))
numero_2 = float (input ("Digite um número: "))
# Chamando a função
resultado = maior_numero (numero_1,numero_2)
# Apresentando o resultado
print ( f"O maior númrero digitado foi: {resultado}")