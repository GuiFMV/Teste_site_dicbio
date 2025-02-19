import json

# Carregar os arquivos JSON
with open("JSONs/DataframePrincipal.json", "r", encoding="utf-8") as file1:
    dataframe_principal = json.load(file1)

with open("JSONs/resultado.json", "r", encoding="utf-8") as file2:
    resultado = json.load(file2)

# Converter 'resultado' para um dicionário com base no 'SenseNumber'
resultado_dict = {
    item['DefinitionData']['SenseNumber']: item
    for item in resultado
    if item.get('DefinitionData') and item['DefinitionData'].get('SenseNumber') is not None
}

# Combinar os arquivos com base no 'sensenumber'
mesclados = []
for entry in dataframe_principal:
    sense_number = entry.get('sensenumber')
    if sense_number in resultado_dict:
        mesclado = {
            **entry,
            "resultado_data": resultado_dict[sense_number]
        }
        mesclados.append(mesclado)
    else:
        mesclados.append(entry)

# Salvar o arquivo combinado
with open("JSONs/mesclados.json", "w", encoding="utf-8") as output_file:
    json.dump(mesclados, output_file, ensure_ascii=False, indent=4)

print("Mesclagem concluída. Arquivo salvo como 'mesclados.json'.")
