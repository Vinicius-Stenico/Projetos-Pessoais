import math
import tkinter as tk

# Mostra o tamanho da janela
# def mostrar_tamanho():
#     largura = janela.winfo_width()
#     altura = janela.winfo_height()
#     print(f"Tamanho da janela: {largura}x{altura}")
#     janela.after(200, mostrar_tamanho)

# Variáveis Globais
n1 = None # Variável para guardar o primeiro número das operações
operador = None # Variável para guardar o operador atual
resultado_mostrado = False # Variável para saber se o resultado já foi mostrado
novo_numero = False # Variável para saber se um novo número foi digitado no visor
# Função para formatar número
def formatar_numero(num):
    if float(num).is_integer():
        return str(int(num))
    return str(num)
# Dicionário de operações binárias básicas
operacoes = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "X": lambda a, b: a * b,
    "÷": lambda a, b: a / b if b != 0 else float("nan")
}
# Dicionário de porcentagem (operação binária) e operações unárias
operacoes_especiais = {
   "%": lambda a, b: a * b /100,
   "√": lambda a: math.sqrt(a),
   "x²": lambda a: a**2,
   "1/x": lambda a: 1/a if a != 0 else float("nan")
}
# Função para inserir números no visor da calculadora
def inserir_numero(botao):
    global resultado_mostrado, novo_numero

    visor = entrada.get()

    # Atualiza o visor após ter mostrado o resultado
    if resultado_mostrado:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, botao)
        placeholder.config(text="")
        resultado_mostrado = False
        novo_numero = False
    # Atualiza o visor após apertar o botão de operação
    elif novo_numero:
        if visor == botao:
            entrada.insert(tk.END, botao)
        else:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, botao)
        novo_numero = False
    else: 
        if visor == "0":
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, botao)
        else:
            entrada.insert(tk.END, botao)
# Função de configurar placeholder após apertar operador (+-X÷)
def clicar_operador(botao):
    global n1, operador, resultado_mostrado, novo_numero
    try:
        valor_atual = float(entrada.get())
        expressao = placeholder.cget("text").strip()
        texto_final = expressao
        operadores_validos = ["+", "-", "X", "÷"]

        # Caso especial: Trocar de operador (ex: clicou +, depois -)
        if expressao and expressao.split()[-1] in operadores_validos:
            if valor_atual == n1:
                partes = expressao.split()
                partes[-1] = botao
                placeholder.config(text=" ".join(partes))
                operador = botao
                return # Apenas troca o operador, sem recalcular nada
            else:
                partes = expressao.split()
                partes[-1] = botao
                texto_final = " ".join(partes)
                placeholder.config(text=texto_final)
                operador = botao

        # Se ainda não há operador definido (primeira operação)
        if operador is  None:
            n1 = valor_atual
            ultimo_numero = valor_atual
      
        else:  
            partes = expressao.split()
            ultimo_operador_util = None

            # Encontra o último operador com número à direita
            for i in range(len(partes) - 1):
                if partes[i] in operadores_validos and partes[i + 1] not in operadores_validos:
                    ultimo_operador_util = partes[i]
                print(ultimo_operador_util)

            if ultimo_operador_util:
                if not novo_numero:
                    n1 = operacoes[ultimo_operador_util](n1, valor_atual)
                    ultimo_numero = valor_atual
                elif ultimo_numero is not None:
                    n1 = operacoes[ultimo_operador_util](n1, ultimo_numero) 
            else:
                operador = partes[1]
                if not novo_numero:
                    n1 = operacoes[operador](n1, valor_atual)
                    ultimo_numero = valor_atual
                elif ultimo_numero is not None:
                    n1 = operacoes[operador](n1, ultimo_numero) 
            entrada.delete(0, tk.END)
            entrada.insert(0, formatar_numero(n1))

        if expressao:
            operador = botao
            nova_expressao = (f"{expressao} {formatar_numero(valor_atual)} {operador}")
            placeholder.config(text=nova_expressao)
            resultado_mostrado = False
            novo_numero = True
        else:    
            operador = botao
            placeholder.config(text=f"{formatar_numero(n1)} {operador}")
            resultado_mostrado = False
            novo_numero = True  
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "0")
        
# Função de calcular resultado da porcentagem e operações unárias
def aplicar_especial(botao):
    global n1
    try:
        valor = float(entrada.get())
        if botao == "%"and n1 is not None:
            resultado = operacoes_especiais["%"](n1, valor)
            placeholder.config(text=f"{formatar_numero(n1)} {botao} {formatar_numero(valor)}")
        else:
            resultado = operacoes_especiais[botao](valor)
            placeholder.config(text=f"{botao}({formatar_numero(valor)})")
        
        entrada.delete(0, tk.END)
        entrada.insert(0, formatar_numero(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")
# Função de calcular o resultado das operações binárias básicas
def calcular_resultado():
    global n1, operador, resultado_mostrado, novo_numero
    if operador and n1 is not None:
        try:
            n2 = float(entrada.get())
            resultado = operacoes[operador](n1, n2)
            entrada.delete(0, tk.END)
            entrada.insert(0, formatar_numero(resultado))
            placeholder.config(text=f"{formatar_numero(n1)} {operador} {formatar_numero(n2)} =")
            n1 = resultado
            resultado_mostrado = True
            operador = None
        except Exception as e:
            entrada.delete(0, tk.END)
            entrada.insert(0, "0")
# Função de configuração de botões utéis na calculadora    
def outros(botao):
    global n1, operador, resultado_mostrado, novo_numero
    # Botão C
    if botao == "C":
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")
        placeholder.config(text="")
        n1 = None
        operador = None
        resultado_mostrado = False
    # Botão CE
    elif botao == "CE":
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")
    # Botão +/-
    elif botao == "+/-":
        n1 = float(entrada.get())
        n1 = -n1
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(n1))
    # Botão ⌫
    elif botao == "⌫":
        texto = entrada.get()
        if len(texto) > 1:
            entrada.delete(len(texto)-1, tk.END)
        else:
            entrada.delete(0, tk.END)
            entrada.insert(0, "0")
# Função clicar que chama as outras funções
def clicar(botao):
    if botao in "0123456789.":
        inserir_numero(botao)
    elif botao in "+-X÷":
        clicar_operador(botao)
    elif botao == "=":
        calcular_resultado()
    elif botao in ["%", "√", "x²", "1/x"]:
        aplicar_especial(botao)
    elif botao in ["C", "CE", "+/-", "⌫"]:
        outros(botao)

janela = tk.Tk()

janela.title("Calculadora")

janela.geometry("320x500")
# Configuração do placeholder
placeholder = tk.Label(janela, text="", anchor="e", font=("Arial", 12), fg="gray")
placeholder.grid(row=0, column=0, columnspan=4, padx=10, pady=(10,0), sticky="nsew")

# Visor da calculadora
entrada = tk.Entry(janela, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

entrada.insert(0, "0")

botoes = [
    ("%", 2, 0), ("√", 2, 1), ("x²", 2, 2), ("1/x", 2, 3),
    ("CE", 3, 0), ("C", 3, 1), ("⌫", 3, 2), ("÷", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("X", 4, 3),
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("-", 5, 3),
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("+", 6, 3),
    ("+/-", 7, 0), ("0", 7, 1), (".", 7, 2), ("=", 7, 3),
]

for (texto, linha, coluna) in botoes:
    botao = tk.Button(janela, text=texto, font=("Arial", 16), width=5, height=2, command=lambda t=texto: clicar(t))
    botao.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)

for i in range(5):
    janela.grid_rowconfigure(i, weight=1)
    janela.grid_columnconfigure(i, weight=1)

# Vincula o evento de redimensionar
# mostrar_tamanho()

janela.mainloop()