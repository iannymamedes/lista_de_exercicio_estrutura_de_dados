# Escreva uma função chamada TPilha2 que recebe como parâmetro 2
# pilhas (N e P) e um vetor de inteiros. Para cada um:
# - se positivo, inserir na pilha P;
# - se negativo, inserir na pilha N;
# - se zero, retirar um elemento de cada pilha.

def TPilha2(N:list,P:list,vetor:list):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                N.pop()
            if len(P) > 0:
                P.pop()

        elif vetor[i] > 0:
            P.append(vetor[i])

        else:
            N.append(vetor[i])

    print(N,P)

x = TPilha2([],[],[-1,1,-2,2,0])