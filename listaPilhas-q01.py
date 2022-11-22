# Escrever uma função que receba como parâmetro uma pilha.
# A função deve retornar o maior elemento da pilha. A passagem deve ser por valor ou referência?


def maior_elemento(pilha):
    maior = pilha[0]
    for i in range(len(pilha)):
        if pilha[i] > maior:
            maior = pilha[i]
    return maior

p = maior_elemento([7, 10, 3, 22, 33])
print(p)