import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")



resultado = requisicao.json()

print(f"O valor atual da cotação é de R$ {resultado["USDBRL"]['high']}")