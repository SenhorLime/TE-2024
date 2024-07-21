import tkinter as tk
from tkinter import ttk
import csv

# Função para salvar os dados no arquivo CSV
def salvar_dados():
    id_carro = entry_id.get()
    fabricante = entry_fabricante.get()
    modelo = entry_modelo.get()
    ano = entry_ano.get()

    with open('carros.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([id_carro, fabricante, modelo, ano])

    limpar_campos()

# Função para limpar o conteúdo das caixas de texto
def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_fabricante.delete(0, tk.END)
    entry_modelo.delete(0, tk.END)
    entry_ano.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Carro")

# Frame para organização
frame = ttk.Frame(root, padding="20")
frame.grid()

# Labels e Entradas para os dados do carro
lbl_id = ttk.Label(frame, text="ID:")
lbl_id.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_id = ttk.Entry(frame)
entry_id.grid(row=0, column=1, padx=10, pady=5)

lbl_fabricante = ttk.Label(frame, text="Fabricante:")
lbl_fabricante.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_fabricante = ttk.Entry(frame)
entry_fabricante.grid(row=1, column=1, padx=10, pady=5)

lbl_modelo = ttk.Label(frame, text="Modelo:")
lbl_modelo.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_modelo = ttk.Entry(frame)
entry_modelo.grid(row=2, column=1, padx=10, pady=5)

lbl_ano = ttk.Label(frame, text="Ano:")
lbl_ano.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_ano = ttk.Entry(frame)
entry_ano.grid(row=3, column=1, padx=10, pady=5)

# Botão para salvar os dados
btn_salvar = ttk.Button(frame, text="Salvar", command=salvar_dados)
btn_salvar.grid(row=4, column=0, padx=10, pady=10)

# Botão para limpar os campos de entrada
btn_limpar = ttk.Button(frame, text="Limpar", command=limpar_campos)
btn_limpar.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
