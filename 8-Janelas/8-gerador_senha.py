#Importando a biblioteca e nomeando de tk
import tkinter as tk
ALTURA =   "450" 
LARGURA = "400"

# Função temporária apenas para testar
def aca_clique():
    print ("O botão foi clicado!")

#====================================
#1. Configuração da janela Principal
#====================================
janela = tk.Tk ()
janela.title ("Strong Password")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#414042")


#==========================================
#2. Título principal do aplicativo na tela 
#==========================================
titulo = tk.Label (
    text=" SecuroServ Password",
    font =("Arial",16,"bold"),
    bg="#414042",
    fg= "#E6E1DF"
)
titulo.pack(pady=20)
"""
logo = tk.PhotoImage(file="logo.png")
label_logo = tk.Label(janela,image=logo)
label_logo.pack(pady=20)
"""
#===========================================
#3. Criando Label do tamanho da Senha
#===========================================
lbl_tamanho_senha = tk.Label (
    text="  Tamanho da Senha ",
    font =("Arial",16),
    bg="#414042",
    fg= "#FF0400"
)
lbl_tamanho_senha.pack(pady=12)

#==============================================
#4. Criando a entrada da Senha
#==============================================
entry_tamanho_senha = tk.Entry(
    janela,
    font=("Copperplate Gothic",12),
    width=10,
    justify="center"
)
entry_tamanho_senha.pack(pady=5)

#====================================================
#5. Criando as variáveis de controle true or false
#====================================================
var_maiusculo = tk.BooleanVar (value=True)
var_minusculo = tk.BooleanVar (value=True)
var_numeros = tk.BooleanVar (value=True)
var_simbolos = tk.BooleanVar (value=False)

# Criando as caixinhas de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text= "Maiúsculas (A-Z)",
    variable= var_maiusculo,
    bg="#414042",
    fg="#ffffff",
    selectcolor="#414042",
    activebackground= "#414042",
    activeforeground="#ffffff"
)
chk_maiuscula.pack(anchor ="w", padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text= "Minúsculas (a-z)",
    variable= var_minusculo,
    bg="#414042",
    fg="#ffffff",
    selectcolor="#414042",
    activebackground= "#414042",
    activeforeground="#ffffff"
)
chk_minuscula.pack(anchor ="w", padx=60, pady=2)

chk_numeros = tk.Checkbutton(
    janela,
    text= "Números (0-9)",
    variable= var_numeros,
    bg="#414042",
    fg="#ffffff",
    selectcolor="#414042",
    activebackground= "#414042",
    activeforeground="#ffffff"
)
chk_numeros.pack(anchor ="w", padx=60, pady=2)

chk_simbolos = tk.Checkbutton(
    janela,
    text= "Caracteres Especiais (@#.,) ",
    variable= var_simbolos,
    bg="#414042",
    fg="#ffffff",
    selectcolor="#414042",
    activebackground= "#414042",
    activeforeground="#ffffff"
)
chk_simbolos.pack(anchor ="w", padx=60, pady=2)








janela.mainloop()