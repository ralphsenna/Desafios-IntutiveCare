import tabula
from zipfile import ZipFile, ZIP_DEFLATED

zip = ZipFile("Arquivos.zip", "r")
zip.extract("Anexo I - Lista completa de procedimentos.pdf")
zip.close()

pdf_path = "Anexo I - Lista completa de procedimentos.pdf"
tabula.convert_into(pdf_path, "Teste_Rafael.csv", pages="all", output_format="csv", stream=True)

# Bônus do Desafio
csv = open("Teste_Rafael.csv")
linhas = csv.readlines()
for linha in linhas:
    linha.replace("OD", "Seg. Odontológica")
    linha.replace("AMB", "Seg. Ambulatorial")
csv.writelines(linhas)
csv.close()

zip = ZipFile("Teste_Rafael.zip", "w", compression=ZIP_DEFLATED)
zip.write("Teste_Rafael.csv")
zip.close()
