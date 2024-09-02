"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP  R$67.836,43
• RJ  R$36.678,66
• MG  R$29.229,88
• ES  R$27.165,48
• Outros  R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

"""


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