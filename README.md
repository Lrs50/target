# Desafio Target Sistemas

Este repositório contém a solução desenvolvida para o desafio técnico proposto pela empresa Target.

1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

```
def main():

    INDICE,SOMA,K = 13,0,0
    
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(SOMA)

if __name__ == "__main__":
    main()
```

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

```
def fib(n):
    r0 = 0
    r1 = 1

    while r1 < n:
        r1 += r0
        r0 = r1 - r0
    
    return (n==r1 or n==r0)

def main():

    N = 144

    if fib(N):
        print(f" O número {N} pertence a sequência de Fibonacci!")
    else:
        print(f" O número {N} não pertence a sequência de Fibonacci!")

if __name__ == "__main__":
    main()

```

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

```

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
```

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

```
def main():

    data = {"SP":67836.43,
            "RJ":36678.66,
            "MG":29229.88,
            "ES":27165.48,
            "Outros":19849.53}

    total = 0
    for d in data.values():
        total += d

    print("Percentual de Representação por Estado")
    for state,v in data.items():
        print(f"{state} - {v/total:.2%}")

if __name__ == "__main__":
    main()
```

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

```
from collections import deque

def main():
    txt = "Qualquer tecnologia suficientemente avançada é indistinguível da magia"

    print(txt[::-1]) # Maneira Pythonica

    # deques são eficientes 
    inv_txt = deque()
    for c in txt:
        inv_txt.appendleft(c)

    print(''.join(inv_txt))

if __name__ == "__main__":
    main()
```