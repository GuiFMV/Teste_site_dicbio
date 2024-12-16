import tkinter as tk
from tkinter import filedialog
import pandas as pd

def convert_csv_to_json(file_path):
    try:
        # Lê o arquivo CSV e converte para JSON
        data = pd.read_csv(file_path)
        json_data = data.to_json(orient="records", force_ascii=False, indent=4)  # force_ascii=False permite caracteres especiais

        # Abre um diálogo para escolher onde salvar o arquivo JSON
        save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if save_path:
            with open(save_path, "w", encoding="utf-8") as json_file:
                json_file.write(json_data)
            label_status.config(text=f"Arquivo JSON salvo em: {save_path}")
        else:
            label_status.config(text="Operação cancelada pelo usuário.")
    except Exception as e:
        label_status.config(text=f"Erro: {e}")

# Função para abrir o explorador de arquivos e selecionar o arquivo CSV
def escolher_arquivo_csv():
    file_path = filedialog.askopenfilename(title="Selecione um arquivo CSV", filetypes=[("CSV files", "*.csv")])
    if file_path:
        convert_csv_to_json(file_path)
    else:
        label_status.config(text="Nenhum arquivo CSV selecionado.")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor CSV para JSON")
root.geometry("400x200")

# Instruções para o usuário
label_instruction = tk.Label(root, text="Clique no botão para selecionar um arquivo CSV:")
label_instruction.pack(pady=20)

# Botão para abrir o explorador de arquivos
btn_select_file = tk.Button(root, text="Escolher arquivo CSV", command=escolher_arquivo_csv)
btn_select_file.pack(pady=10)

# Área para exibir status
label_status = tk.Label(root, text="")
label_status.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()
