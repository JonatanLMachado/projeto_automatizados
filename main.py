import tkinter as tk
from tkinter import ttk
from datetime import datetime

from Contract import Contract
from ContractService import ContractService
from PaypalService import PaypalService
from PicpayService import PicpayService

def obtain_date():
    bank_name = combo_bank.get()
    value = float(entry_value.get())
    date = datetime.strptime(entry_date.get(), "%d/%m/%Y").date()
    number = int(entry_number.get())

    contract = Contract(number, date, value)

    if(bank_name == "Paypal"):
        bank = PaypalService()
    else:
        bank = PicpayService()

    # Cria serviço do contrato fazendo o casting a partir do banco contratado
    contractService = ContractService(bank)

    contractService.process_contract(contract, number)

    installments = contract.get_installments()

    return installments

def show_data():
    installments = obtain_date()
    output = f"Simulação do contrato:\n"

    # Criar parcelas do contrato
    total_value = 0.0
    for i in installments:
        date_formatted = i.get_due_date().strftime("%d/%m/%Y")
        value_formatted = format(i.get_amount(), ".2f")
        total_value += float(value_formatted)
        output += f"Data: {date_formatted} ----- Valor: R${value_formatted}\n"

    output += f"----------------------------------------------\n"
    total_value_formatted = format(total_value, ".2f")
    output += f"Valor total do contrato: R${total_value_formatted}\n"

    # Criar uma window pop-up para exibir as informações
    popup = tk.Toplevel(window)
    popup.title("Mais Informações")
    tk.Label(popup, text=output).pack(padx=10, pady=10)

# Opções para as caixas de combinação
opcoes_bank = ["Paypal", "Picpay"]

# Criar a window principal
window = tk.Tk()
window.title("Financiamento Bancário")

# Criar e posicionar widgets na window
tk.Label(window, text="Nome do banco:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Valor:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, text="Data (DD/MM/YYYY):").grid(row=2, column=0, padx=10, pady=10)
tk.Label(window, text="Número de parcelas:").grid(row=3, column=0, padx=10, pady=10)

combo_bank = ttk.Combobox(window, values=opcoes_bank)
entry_value = tk.Entry(window)
entry_date = tk.Entry(window)
entry_number = tk.Entry(window)

combo_bank.grid(row=0, column=1, padx=10, pady=10)
entry_value.grid(row=1, column=1, padx=10, pady=10)
entry_date.grid(row=2, column=1, padx=10, pady=10)
entry_number.grid(row=3, column=1, padx=10, pady=10)

# Botão para exibir os dados
btn_show_data = tk.Button(window, text="Simular valor das parcelas", command=show_data)
btn_show_data.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()

