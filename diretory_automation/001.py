import shutil 

caminho = r"c:\Users\Gustavo Castro\Downloads\Gustavo_Castro_Curriculo.pdf"
destino = r"C:\Users\Gustavo Castro\Documents\documentos\New folder"



try:
    shutil.copy(caminho,destino)
    print("Arquivo movido para a pasta com sucesso!!")
except Exception as e:
    print("Erro ao tentar processar o documento!!")




