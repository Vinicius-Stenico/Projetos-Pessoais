import math
import tkinter as tk

# Mostra o tamanho da janela
# def mostrar_tamanho():
#     largura = janela.winfo_width()
#     altura = janela.winfo_height()
#     print(f"Tamanho da janela: {largura}x{altura}")
#     janela.after(200, mostrar_tamanho)

n1 = None
operador = None
resultado_mostrado = False
novo_numero = False

def formatar_numero(num):
    if float(num).is_integer():
        return str(int(num))
    return str(num)

def apagar_digito():
    texto = entrada.get()
    if len(texto) > 1:
        entrada.delete(len(texto)-1, tk.END)
    else:
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")

def clicar(botao):
    global n1, operador, resultado_mostrado, novo_numero
    
    if botao == "C":
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")
        placeholder.config(text="")
        n1 = None
        operador = None
        resultado_mostrado = False

    elif botao == "CE":
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")

    elif botao == "+/-":
        n2 = float(entrada.get())
        n2 = -n2
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(n2))

    elif botao == "⌫":
        texto = entrada.get()
        if len(texto) > 1:
            entrada.delete(len(texto)-1, tk.END)
        else:
            entrada.delete(0, tk.END)
            entrada.insert(0, "0")

    elif botao == "=":
        try:
            texto = placeholder.cget("text")
            n1 = float(texto.split()[0])
            n2 = float(entrada.get())
            if operador == "+":
                resultado = n1 + n2
            elif operador == "-":
                resultado = n1 - n2
            elif operador == "X":
                resultado = n1 * n2
            elif operador == "÷":
                if n2 !=0:
                    resultado = n1 / n2
                else:
                    resultado = "Resultado Indefinido"
            else:
                resultado = 0
            
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
            placeholder.config(text="")
            operador = None
            resultado_mostrado = True
        except:
            resultado = 0
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
            resultado_mostrado = True

    elif botao in ["+", "-", "X", "÷"]:
        try:
            n1 = float(entrada.get())
            operador = botao
            expressao = f"{formatar_numero(n1)} {botao}"
            placeholder.config(text=expressao)
            entrada.delete(0, tk.END)
            entrada.insert(0, formatar_numero(n1))
            resultado_mostrado = False
            novo_numero = True
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "0")

    elif botao in ["%", "√", "x²", "1/x"]:
        try:
            operador = botao
            if operador == "%":

                valor_entry = entrada.get().strip()

                if valor_entry == "":
                    raise ValueError("Entry vazio")
            
                n1 = float(valor_entry)

                # verifica se placeholder tem número e operação
                texto = placeholder.cget("text").strip()
                partes = texto.split()
                
                if len(partes) < 2:
                    entrada.delete(0, tk.END)
                    entrada.insert(tk.END, str(0))
                
                n2 = float(partes[0])
                operacao = partes[1]

                

                # calcula porcentagem
                resultado = (n2 * n1) / 100

                # atualiza visor e placeholder
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, str(resultado))
                placeholder.config(text=f"{n2} {operacao} {resultado}")
                

            elif operador == "√":
                n1 = float(entrada.get())
                resultado = math.sqrt(n1)
                
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, str(resultado))
                placeholder.config(text=f"√({n1})")
                
            
            elif operador == "x²":
                n1 = float(entrada.get())
                resultado = math.pow(n1, 2)

                entrada.delete(0, tk.END)
                entrada.insert(tk.END, str(resultado))
                placeholder.config(text=f"sqr({n1})")
                

            elif operador == "1/x":  
                n1 = float(entrada.get())
                resultado = 1 / n1

                entrada.delete(0, tk.END)
                entrada.insert(tk.END, str(resultado))
                placeholder.config(text=f"1/({n1})")
                
            resultado_mostrado = True
    
        except Exception as e:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
            print("Erro %:", e)
            resultado_mostrado = True
        
    else:
    
        visor = entrada.get()
        
        if resultado_mostrado:
            entrada.delete(0,tk.END)
            entrada.insert(tk.END, botao)
            resultado_mostrado = False
            novo_numero = False

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


janela = tk.Tk()

janela.title("Calculadora")

janela.geometry("320x500")

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