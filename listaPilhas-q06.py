# Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles, como segue:
# - se o número for par, insira-o na pilha;
# - se o número lido for ímpar, retire um número da pilha;
# - Ao final, esvazie a pilha imprimindo os elementos.


def TPilha(vetor):
    pilha = []
    
    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] %2 == 0:
                pilha.append(vetor[i])
            else:
                if len(pilha) > 0:
                    pilha.pop()

        for i in range(len(pilha)):
            print(pilha.pop(0))           

x = TPilha([3,2,4,7,1,11,13,15,22,34,56,10,5,8,9])