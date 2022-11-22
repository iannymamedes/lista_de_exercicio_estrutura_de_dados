# Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N &gt;0) números reais, imprimi-la na
# ordem inversa.


def imprimir_inversamente(pilha:list):
    pilha_inversa = []

    for i in pilha[::-1]:
        pilha_inversa.append(i)

    return pilha_inversa

x = imprimir_inversamente([3,5,7,8,9])
print(x)