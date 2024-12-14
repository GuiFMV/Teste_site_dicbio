import sqlite3
import pandas as pd

def visualizar_tabela_sqlite(db_path, table_name):
    try:
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect(db_path)

        # Consulta SQL para pegar todos os dados da tabela
        query = f"SELECT * FROM {table_name};"

        # Usar o pandas para ler os dados diretamente em um DataFrame
        df = pd.read_sql(query, conn)

        # Exibir o conteúdo da tabela
        print(f"Conteúdo da tabela {table_name}:")
        print(df)

    except Exception as e:
        print(f"Erro ao consultar a tabela: {e}")
    finally:
        # Fechar a conexão com o banco de dados
        conn.close()

# Caminho para o banco de dados SQLite
db_file = 'output_database.db'  # Substitua pelo seu caminho de banco de dados
table_name = 'data'  # Substitua pelo nome da sua tabela

# Visualizar a tabela
visualizar_tabela_sqlite(db_file, table_name)
