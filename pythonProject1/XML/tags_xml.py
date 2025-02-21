import xml.etree.ElementTree as ET

# Carregar o arquivo XML
# No meu caso, para encontrar o caminho do arquivo preciso passar o caminho completo da minha pasta e colocar duas
# barras para entender que estou usando uma
tree = ET.parse("C:\\Users\\Guila\\OneDrive\\Documentos\\dicbio\\data\\compendio1brotero.xml")  # Substitua pelo caminho correto
root = tree.getroot()

# for element in root.iter(): # Para teste
#     print(element.tag, element.attrib)

# Encontrar o elemento <body>
body_element = root.find("front") # Escolha o elemento desejado front, body ou back

# Função para extrair todo texto dentro de um elemento


def extract_text(element):
    text = element.text or ""
    for sub_element in element:
        text += extract_text(sub_element) + (sub_element.tail or "")
    return text

# Obter e imprimir o texto dentro de <body>


body_text = extract_text(body_element)
print(body_text)
