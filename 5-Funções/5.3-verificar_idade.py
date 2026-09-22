# Criando função verificar_idade
def verficar_idade (idade):
    if idade >= 18:
        return "Maior de idade"
    else: 
        return "Menor de idade"

    # Solicitando a idade do usuário
idade_usuário =  int (input ("Digite sua idade: "))

resultado = verficar_idade (idade_usuário)

print (resultado)