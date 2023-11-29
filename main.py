import tkinter as tk
from tkinter import ttk
from datetime import datetime

from Contract import Contract
from ContractService import ContractService
from PaypalService import PaypalService
from PicpayService import PicpayService

def obter_dados():
    nome_banco = combo_banco.get()
    valor = float(entry_valor.get())
    data = datetime.strptime(entry_data.get(), "%d/%m/%Y").date()
    numero = int(entry_numero.get())

    contract = Contract(numero, data, valor)

    if(nome_banco == "Paypal"):
        banco = PaypalService()
    else:
        banco = PicpayService()

    contractService = ContractService(banco)

    contractService.process_contract(contract, numero)

    installments = contract.get_installments()

    return installments

def exibir_dados():
    installments = obter_dados()
    mensagem = f"Simulação do contrato:\n"

    total_value = 0.0
    for i in installments:
        date_formatted = i.get_due_date().strftime("%d/%m/%Y")
        value_formatted = format(i.get_amount(), ".2f")
        total_value += float(value_formatted)
        mensagem += f"Data: {date_formatted} ----- Valor: R${value_formatted}\n"

    mensagem += f"--------------------------------------\n"
    total_value_formatted = format(total_value, ".2f")
    mensagem += f"Valor total do contrato: R${total_value_formatted}\n"

    # Criar uma janela pop-up para exibir as informações
    popup = tk.Toplevel(janela)
    popup.title("Mais Informações")
    tk.Label(popup, text=mensagem).pack(padx=10, pady=10)

# Opções para as caixas de combinação
opcoes_banco = ["Paypal", "Picpay"]

# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Transação Bancária")

# Criar e posicionar widgets na janela
tk.Label(janela, text="Nome do Banco:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(janela, text="Valor:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(janela, text="Data (DD/MM/YYYY):").grid(row=2, column=0, padx=10, pady=10)
tk.Label(janela, text="Número de parcelas:").grid(row=3, column=0, padx=10, pady=10)

combo_banco = ttk.Combobox(janela, values=opcoes_banco)
entry_valor = tk.Entry(janela)
entry_data = tk.Entry(janela)
entry_numero = tk.Entry(janela)

combo_banco.grid(row=0, column=1, padx=10, pady=10)
entry_valor.grid(row=1, column=1, padx=10, pady=10)
entry_data.grid(row=2, column=1, padx=10, pady=10)
entry_numero.grid(row=3, column=1, padx=10, pady=10)

# Botão para exibir os dados
btn_exibir_dados = tk.Button(janela, text="Simular valor das parcelas", command=exibir_dados)
btn_exibir_dados.grid(row=4, column=0, columnspan=2, pady=10)

janela.mainloop()

