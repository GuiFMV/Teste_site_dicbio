import tkinter as tk
from tkinter import filedialog, messagebox
import json
import sqlite3
import pandas as pd


def json_to_sqlite(json_path, db_path):
    try:
        # Ler o arquivo JSON
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Converte para DataFrame (supondo que o JSON seja uma lista de objetos)
        df = pd.DataFrame(data)

        # Conectar ao banco de dados SQLite (ou criar um novo)
        conn = sqlite3.connect(db_path)

        # Criar a tabela no banco de dados com base nos dados
        table_name = "data"  # Nome da tabela (mude conforme necessário)
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        messagebox.showinfo(title="Sucesso!", message=f"Dados inseridos com sucesso no banco de dados: {db_path}")
    except Exception as e:
        messagebox.showwarning(f"Erro ao processar: {e}")
    finally:
        conn.close()


# Função para abrir o explorador de arquivos e selecionar o arquivo JSON
def selecionar_arquivo_json():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    file_path = filedialog.askopenfilename(title="Selecione um arquivo JSON", filetypes=[("JSON Files", "*.json")])
    return file_path


# Função para abrir o explorador de arquivos e salvar o arquivo DB
def selecionar_arquivo_db():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    db_path = filedialog.asksaveasfilename(title="Selecione o local para salvar o banco de dados",
                                           defaultextension=".db", filetypes=[("SQLite DB", "*.db")])
    return db_path


# Função para perguntar se o usuário deseja processar mais um arquivo
def perguntar_continuar():
    resposta = messagebox.askquestion("Continuar",
                                      "Deseja escolher mais um arquivo JSON para transformar em banco de dados?")
    return resposta == 'yes'


# Função principal que gerencia o fluxo do programa
def iniciar_programa():
    while True:
        # Seleciona o arquivo JSON
        json_file = selecionar_arquivo_json()

        # Se não houver arquivo selecionado, encerra o programa
        if not json_file:
            break

        # Seleciona o local para salvar o arquivo DB
        db_file = selecionar_arquivo_db()

        # Usa o nome do arquivo JSON para gerar o nome do banco de dados automaticamente
        db_file = db_file if db_file else json_file.replace('.json', '.db')

        # Executa a conversão para SQLite
        if json_file and db_file:
            json_to_sqlite(json_file, db_file)

        # Pergunta se o usuário quer processar outro arquivo
        if not perguntar_continuar():
            break  # Sai do loop e encerra o programa


# Inicia o programa
iniciar_programa()
