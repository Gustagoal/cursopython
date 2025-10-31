import PyPDF2
import shutil

# Caminho do PDF
caminho = r"C:\Users\Gustavo Castro\Desktop\cursopython\arquivos-pdf\cv_gustavo_de_castro_oliveira_gustavo.pdf"

arquivo = PyPDF2.PdfReader(caminho)
# Seleciona a pagina/bloco
pagina = arquivo.pages[0]
# Faz a leitura da pagina/Bloco
leitura = pagina.extract_text()

# Convertendo o arquivo para extensão TXT
with open ("curriculo.txt","w") as arquivo:
    arquivo.write(leitura)


# Utilizando a ferramenta Shutil 
caminho = "curriculo.txt"
destino = r"C:\Users\Gustavo Castro\Desktop\cursopython\arquivos-pdf"
shutil.move(caminho,destino) # move o arquivo para outra pasta 