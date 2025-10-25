# Pegando dados do CHATGPT
from requests import request


requisicao  = request("GET","https://chatgpt.com/")


print(requisicao.text)