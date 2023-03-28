import json
from statistics import mean

with open("dados.json", encoding='utf-8')  as meu_json:
    dados = json.load(meu_json)

faturamentos = []

for i in range(len(dados)):
    if dados[i]['valor'] > 0:
        faturamentos.append(dados[i]['valor'])

cont = 0
for i in range(len(faturamentos)):
    if faturamentos[i] > mean(faturamentos):
        cont += 1
print("A quantidade de dias em que o valor do faturamento diario foi supeerior a media mesal foi: ", cont)

menorValor = min(dados, key=lambda x: x['valor'])
print("O menor valor de faturamento em um dia foi: ",  menorValor['valor'])

maiorValor  = max(dados, key=lambda x: x['valor'])
print("O maior valor de faturamento em um dia foi: ", maiorValor['valor'])


