"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

"""

import json

def main():

    with open('company.json', 'r') as file:
        data = json.load(file)

    min = 0
    max = 0
    total = 0
    n_valid = len(data)
    for i,info in enumerate(data):
        amount = info["earnings"]
        total += amount
        if amount > data[max]['earnings']:
            max = i
        if amount < data[min]['earnings']:
            min = i
        
        if amount == 0:
            n_valid-=1

    avg = total/n_valid
    n = 0

    for info in data:
        amount = info["earnings"]
        if amount > avg:
            n+=1

    print(f"O dia de maior faturamento foi o dia {data[max]['date']} {data[max]['earnings']:7d}$")
    print(f"O dia de menor faturamento foi o dia {data[min]['date']} {data[min]['earnings']:7d}$")
    print(f"A media de lucro diario foi de {avg:7.2f} sendo que durante {n:2d} dias tivemos um valor de lucro maior que a média")

if __name__ == "__main__":
    main()