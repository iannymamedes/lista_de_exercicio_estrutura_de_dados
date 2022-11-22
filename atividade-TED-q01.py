# Construa uma Pilha utilizando a linguagem Python. Dada uma sequência contendo N (N>0)
# números inteiros, imprimi-la na ordem inversa.

import numpy as np


class Pilha:
    def __int__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.topo == self.capacidade - 1:
            return True
        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha está cheia!")
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia!")
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def imprimir_inverso(self):
        pilha_inversa = []
        for i in self.valores[::-1]:
            pilha_inversa.append(i)

        return pilha_inversa


if __name__ == "__main__":
    pilha = Pilha()
    pilha.empilhar(1)
    pilha.empilhar(3)
    pilha.empilhar(5)
    pilha.empilhar(7)

    print(pilha.imprimir_inverso())
