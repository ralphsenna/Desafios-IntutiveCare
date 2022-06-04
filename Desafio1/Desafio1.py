import os
from urllib import request
from zipfile import ZipFile, ZIP_DEFLATED

file_url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/copy2_of_Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.pdf'
name = 'Arquivos/Anexo I - Lista completa de procedimentos.pdf'
request.urlretrieve(file_url, name)

file_url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/copy_of_Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537.xlsx'
name = 'Arquivos/Anexo I - Lista completa de procedimentos.xlsx'
request.urlretrieve(file_url, name)

file_url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_II__DUT_2021_RN_465.2021_tea.br_RN473_RN477_RN478_RN480_RN513_RN536_RN537.pdf'
name = 'Arquivos/Anexo II - Diretrizes de utilização.pdf'
request.urlretrieve(file_url, name)

file_url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_III_DC_2021_RN_465.2021.v2.pdf'
name = 'Arquivos/Anexo III - Diretrizes clínicas.pdf'
request.urlretrieve(file_url, name)

file_url = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_IV_PROUT_2021_RN_465.2021.v2.pdf'
name = 'Arquivos/Anexo IV - Protocolo de utilização.pdf'
request.urlretrieve(file_url, name)

file_names = os.listdir('Arquivos')
zip = ZipFile("Arquivos.zip", "w", compression=ZIP_DEFLATED)
for name_file in file_names:
    zip.write("Arquivos/"+name_file, name_file)
zip.close
