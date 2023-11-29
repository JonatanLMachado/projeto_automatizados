import tkinter as tk
from tkinter import ttk

def obter_dados():
    nome_banco = combo_banco.get()
    valor = entry_valor.get()
    data = entry_data.get()
    operacao = combo_operacao.get()

    # Criar uma lista com os dados
    dados = [nome_banco, valor, data, operacao]

    # Retornar a lista
    return dados

def exibir_dados():
    dados = obter_dados()
    mensagem = "Dados da transação:\n"
    for i, dado in enumerate(dados, start=1):
        mensagem += f"{i}. {dado}\n"

    # Criar uma janela pop-up para exibir as informações
    popup = tk.Toplevel(janela)
    popup.title("Mais Informações")
    tk.Label(popup, text=mensagem).pack(padx=10, pady=10)

# Opções para as caixas de combinação
opcoes_banco = ["Banco A", "Banco B", "Banco C"]
opcoes_operacao = ["Depósito", "Retirada", "Transferência"]

# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Transação Bancária")

# Criar e posicionar widgets na janela
tk.Label(janela, text="Nome do Banco:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(janela, text="Valor:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(janela, text="Data:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(janela, text="Operação:").grid(row=3, column=0, padx=10, pady=10)

combo_banco = ttk.Combobox(janela, values=opcoes_banco)
entry_valor = tk.Entry(janela)
entry_data = tk.Entry(janela)
combo_operacao = ttk.Combobox(janela, values=opcoes_operacao)

combo_banco.grid(row=0, column=1, padx=10, pady=10)
entry_valor.grid(row=1, column=1, padx=10, pady=10)
entry_data.grid(row=2, column=1, padx=10, pady=10)
combo_operacao.grid(row=3, column=1, padx=10, pady=10)

# Botão para exibir os dados
btn_exibir_dados = tk.Button(janela, text="Mostrar Informações", command=exibir_dados)
btn_exibir_dados.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()
