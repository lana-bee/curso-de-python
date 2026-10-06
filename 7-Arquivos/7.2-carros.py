import csv

dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["Suburbano","Itapevi","São Paulo","00366003"],
    ["Av Pedr Paulino","Itapevi","São Paulo","0036604"],
    ["Alto da Colina","Itapevi","São Paulo","00366304"]
    
    ]

with open("7.02-cidades,csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerows(dados_tabela)