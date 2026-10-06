nome = str(input ("Digite seu nome: "))
email = str(input ("Digite seu e-mail: "))

arquivo = open ("7-pessoas.txt", "a",encoding="utf-8")
arquivo.write(f"{nome}, |, {email}, \n")
arquivo.close()

with open ("7-pessoas.txt","a") as arquivo:
    arquivo.write(f"{nome} | {email} \n")