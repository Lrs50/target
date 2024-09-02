"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 
2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na 
linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne 
uma mensagem avisando se o número informado pertence ou não a sequência.
"""

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