from ast import If
from http.client import responses
import requests

#Link público com valor atual da cotação do Dólar
url =  'https://economia.awesomeapi.com.br/all/USD-BRL'

#Busca os dados
response = requests.get(url)

#Se a busca funcionou, mostrar valor da cotação do Dólar
if response.status_code == 200:
    dolar_value = response.json()['USD']['low']
    print(f'O valor do Dólar é R${dolar_value}')
else:
    print('Erro ao buscar valor do Dólar!')