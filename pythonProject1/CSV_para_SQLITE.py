import sqlite3
import pandas as pd

# Caminho para o arquivo CSV e o banco de dados SQLite
csv_file = 'C:\\Users\\Guila\\OneDrive\\Documentos\\dicbio\\data\\DadosDoDicionario.csv'
db_file = 'dicionario.db'

# Carregar os dados do CSV em um DataFrame do Pandas
data = pd.read_csv(csv_file)

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Criar a tabela (ajuste os tipos de dados, se necessário)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Dicionario (
    ID INTEGER PRIMARY KEY,
    Headword TEXT,
    FirstAttestationDate TEXT,
    FirstAttestationExampleMD TEXT,
    Etymology TEXT,
    WClass TEXT,
    Credits TEXT,
    DateOfCreation TEXT,
    DateOfUpdate TEXT
)
''')

# Inserir os dados do CSV no banco de dados
for _, row in data.iterrows():
    cursor.execute('''
    INSERT INTO Dicionario (
        ID, Headword, FirstAttestationDate, FirstAttestationExampleMD,
        Etymology, WClass, Credits, DateOfCreation, DateOfUpdate
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(row))

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()

print("Dados importados com sucesso para o banco de dados SQLite!")
