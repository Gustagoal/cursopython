from pathlib import Path
import shutil , time

pasta = Path(r"C:\Users\Gustavo Castro\Documents\documentos\documentos")

caminho_pdf = r"C:\Users\Gustavo Castro\Desktop\CERTIFICADOS_TESTES"
caminho_txt = r"C:\Users\Gustavo Castro\Desktop\TESTES_TXT"

while True:
    for arquivo in pasta.iterdir():
        if arquivo.suffix == ".pdf":
            shutil.copy(arquivo, caminho_pdf)

        elif arquivo.suffix == ".jpg":
            shutil.copy(arquivo, caminho_txt)
sleep(5)
