import xml.etree.ElementTree as ET

# Carregar o arquivo XML
tree = ET.parse("C:\\Users\\Guila\\OneDrive\\Documentos\\dicbio-TEI-XML\\data\\compendio1brotero.xml")
root = tree.getroot()

# Converter o XML para string formatada
xml_str = ET.tostring(root, encoding="unicode")

# Imprimir o conteúdo XML
print(xml_str)
