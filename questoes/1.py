"""
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
"""


def main():

    INDICE,SOMA,K = 13,0,0
    
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print(SOMA)


if __name__ == "__main__":
    main()