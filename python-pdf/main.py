import PyPDF2
import os 

mesclar = PyPDF2.PdfMerger()

arquivos = os.listdir("arquivos-pdf")

for arquivo in arquivos:
    mesclar.append(f"arquivos-pdf/{arquivo}")



mesclar.write("pdf_junto.pdf")

print("Arquivo junto com sucesso")