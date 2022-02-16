import requests
import json
requisicao = requests.get("https://economia.awesomeapi.com.br/all/")
# pegando dados da api
cotacao = requisicao.json()
moeda_real = float(input("Digite um valor em real para ser convertido: "))
dolar = float(cotacao['USD']["bid"])
euro = float(cotacao['EUR']["bid"])
peso_arg = float(cotacao['ARS']["bid"])
print(f'''R${moeda_real} em Dólar é: US${moeda_real/dolar:.2f}, Euro: €{moeda_real/euro:.2f} 
e em Peso Argentino: ${moeda_real/peso_arg:.2f} ''')
