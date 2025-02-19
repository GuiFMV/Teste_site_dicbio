import json

# Carregar os arquivos JSON
with open("JSONs/DataframePrincipal.json", "r", encoding="utf-8") as file1:
    dataframe_principal = json.load(file1)

with open("JSONs/resultado.json", "r", encoding="utf-8") as file2:
    resultado = json.load(file2)

# Converter 'DataframePrincipal' em um dicionário baseado no 'sensenumber'
dataframe_dict = {}
for item in dataframe_principal:
    sense_number = item.get("sensenumber")
    if sense_number is not None:
        dataframe_dict[sense_number] = item

# Incorporar dados do 'DataframePrincipal' no 'resultado'
resultado_atualizado = []
for item in resultado:
    definition_data = item.get('DefinitionData')
    if definition_data and definition_data.get('SenseNumber') is not None:
        sense_number = definition_data['SenseNumber']
        if sense_number in dataframe_dict:
            # Adicionar dados do DataframePrincipal
            item['DataframePrincipal'] = dataframe_dict[sense_number]
        else:
            # Caso não haja correspondência, o campo será None
            item['DataframePrincipal'] = None
    else:
        # Caso DefinitionData esteja ausente ou incompleto
        item['DataframePrincipal'] = None

    resultado_atualizado.append(item)

# Salvar o arquivo atualizado
with open("JSONs/resultado_atualizado.json", "w", encoding="utf-8") as output_file:
    json.dump(resultado_atualizado, output_file, ensure_ascii=False, indent=4)

print("Atualização concluída. Arquivo salvo como 'resultado_atualizado.json'.")
