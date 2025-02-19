import json

# Caminhos dos arquivos
input_path = 'JSONs/definitions.json'


def remover_campo_id(input_path):
    try:
        # Ler o arquivo JSON
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Remover o campo 'ID_definitions' de cada entrada, trocando o nome remove qualquer classe
        for item in data:
            if 'ID_definitions' in item:
                del item['ID_definitions']

        # Salvar o arquivo atualizado
        with open(input_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Campo 'ID_definitions' removido com sucesso.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")


# Executar a função
remover_campo_id(input_path)
