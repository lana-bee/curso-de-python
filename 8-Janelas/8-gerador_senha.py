# Importando as bibliotecas
import tkinter as tk
import random
import string

ALTURA = "5050"
LARGURA = "400"


# ===================================
# 7. Funções do sistema (A lógica)
# ===================================
def gerar_senha():
    try:
        tamanho = int(entry_tamanho_senha.get())

        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: mínimo de 4 caracteres!",
                fg="#FF0400"
            )
            return

        caracteres = ""

        if var_maiusculo.get():
            caracteres += string.ascii_uppercase

        if var_minusculo.get():
            caracteres += string.ascii_lowercase

        if var_numeros.get():
            caracteres += string.digits

        if var_simbolos.get():
            caracteres += string.punctuation

        if not caracteres:
            lbl_resultado.config(
                text="Erro: selecione ao menos uma opção!",
                fg="#FF0400"
            )
            return

        senha = "".join(
            random.choice(caracteres)
            for i in range(tamanho)
        )

        lbl_resultado.config(
            text="Senha: " + senha,
            fg="#FFFFFF"
        )

    except ValueError:
        lbl_resultado.config(
            text="Erro: digite um tamanho válido!",
            fg="#FF0400"
        )

        # Gerando a senha
        senha = "".join(
            random.choice(caracteres) for i in range(tamanho)
        )

        # Mostrando a senha na tela
        lbl_resultado.config(
            text=f"Senha: {senha}",
            fg="#E6E1DF"
        )

    except ValueError:
        lbl_resultado.config(
            text="Erro: digite um número válido!",
            fg="#FF0400"
        )
# Criando um botão de copiar senha
def copiar_senha():
    texto_resultado = lbl_resultado.cget("text")
# Colocando requisitos e alternativas
    if "Senha: " in texto_resultado:
        senha_pura = texto_resultado.replace("Senha:","")

        janela.clipboard_clear()
        janela.clipboard_append(senha_pura)
    else:
        lbl_status_copia.config(
            text="Nenhuma senha encontrada",
            fg = "#FF0400"
        )



# ====================================
# 1. Configuração da janela principal
# ====================================
janela = tk.Tk()
janela.title("SecuroServ Password")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#414042")
janela.resizable(False, False)


# ==========================================
# 2. Título principal do aplicativo na tela
# ==========================================
logo = tk.PhotoImage(file="logo.png")
logo = logo.subsample(3, 3)

label_logo = tk.Label(
    janela,
    image=logo,
    bg="#414042"
)
label_logo.pack(pady=0)

titulo = tk.Label(
    janela,
    text="SecuroServ Password",
    font=("Arial", 16, "bold"),
    bg="#414042",
    fg="#E6E1DF"
)
titulo.pack(pady=(0,0))


# ===========================================
# 3. Label do tamanho da senha
# ===========================================
lbl_tamanho_senha = tk.Label(
    janela,
    text="Tamanho da Senha",
    font=("Arial", 16),
    bg="#414042",
    fg="#FF0400"
)
lbl_tamanho_senha.pack(pady=12)


# ==============================================
# 4. Entrada do tamanho da senha
# ==============================================
entry_tamanho_senha = tk.Entry(
    janela,
    font=("Copperplate Gothic", 12),
    width=10,
    justify="center"
)
entry_tamanho_senha.pack(pady=5)


# ====================================================
# 5. Variáveis de controle (True ou False)
# ====================================================
var_maiusculo = tk.BooleanVar(value=True)
var_minusculo = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=False)


# Criando as caixas de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text="Maiúsculas (A-Z)",
    variable=var_maiusculo,
    bg="#414042",
    fg="#FFFFFF",
    selectcolor="#414042",
    activebackground="#414042",
    activeforeground="#FFFFFF"
)
chk_maiuscula.pack(anchor="w", padx=60, pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text="Minúsculas (a-z)",
    variable=var_minusculo,
    bg="#414042",
    fg="#FFFFFF",
    selectcolor="#414042",
    activebackground="#414042",
    activeforeground="#FFFFFF"
)
chk_minuscula.pack(anchor="w", padx=60, pady=2)

chk_numeros = tk.Checkbutton(
    janela,
    text="Números (0-9)",
    variable=var_numeros,
    bg="#414042",
    fg="#FFFFFF",
    selectcolor="#414042",
    activebackground="#414042",
    activeforeground="#FFFFFF"
)
chk_numeros.pack(anchor="w", padx=60, pady=2)

chk_simbolos = tk.Checkbutton(
    janela,
    text="Caracteres especiais (@#.,)",
    variable=var_simbolos,
    bg="#414042",
    fg="#FFFFFF",
    selectcolor="#414042",
    activebackground="#414042",
    activeforeground="#FFFFFF"
)
chk_simbolos.pack(anchor="w", padx=60, pady=2)


# ===========================================
# 6. Botão para gerar a senha
# ===========================================
btn_gerar = tk.Button(
    janela,
    text="Gerar senha segura",
    command=gerar_senha,
    bg="#FFFFFF",
    fg="#414042",
    padx=10,
    pady=5
)
btn_gerar.pack(pady=15)


# Label que apresenta o resultado
lbl_resultado = tk.Label(
    janela,
    text="A senha aparecerá aqui",
    font=("Arial", 11, "bold"),
    bg="#414042",
    fg="#E6E1DF",
    wraplength=350
)
lbl_resultado.pack(pady=5)

btn_copiar = tk.Button (
    janela,
    text= "Copiar",
    command= copiar_senha,
    font= ("Arial",10,"bold"),
    bg= "#FF0400",
    fg= "#ffffff",
    padx=10,
    pady=3
)
btn_copiar.pack(pady=2)
lbl_status_copia = tk.Label(
    janela,
    text="",
    font= ("Arial",9),
    bg= "#414042",
    fg= "#ffffff"
)
lbl_status_copia.pack(pady=2)

# Mantendo a janela aberta
janela.mainloop()