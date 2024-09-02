"""Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

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