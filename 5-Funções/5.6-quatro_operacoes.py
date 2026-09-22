def somar (a,b):
    return a + b

def subtrair (a,b):
    return a - b

def multiplicar (a,b):
    return a * b

def dividir (a,b):
    return a / b

a = float (input("Digite um número: "))
b = float (input("Digite um número: "))

resultado_soma = somar (a,b)
resultado_sub = subtrair (a,b)
resultado_mult = multiplicar (a,b)
resultado_divi = dividir (a,b)

print (f"O resultado da soma é: {resultado_soma}")
print (f"O resultado da subtração é: {resultado_sub}")
print (f"O resultado da multiplicação é: {resultado_mult}")
print (f"O resultado da divisão é: {resultado_divi}")