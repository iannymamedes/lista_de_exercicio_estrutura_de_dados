# Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação problema:
# Armazene as placas dos carros de luxos (apenas os números) que estão estacionados em um rua sem saída.
# Dado uma placa verifique se o carro está estacionado na rua. Caso esteja, informe a sequência de carros
# que deverá ser retirada para que o carro em questão consiga sair.



import numpy as np

class Rua:
    def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultimo_carro = -1
    self.valores = np.empty(self.capacidade, dtype=int)

def __rua_cheia(self):
    if self.ultimo_carro == self.capacidade -1:
        return True
    else: 
        return False

def rua_vazia(self):
    if self.ultimo_carro == -1:
        return True
    else: 
        return False

def estacionar(self, placa):
    if self.__rua_cheia():
        print("A rua está cheia!")
    else:
        self.ultimo_carro += 1
        self.valores[self.ultimo_carro] = placa

def retirar(self):
    if self.rua_vazia():
        print("A rua está vazia!")
        return -1
    else:
        valor = self.valores[self.ultimo_carro]
        self.ultimo_carro -=1
        return valor
    
def ver_ultimo_carro(self):
    if self.ultimo_carro != -1:
        return self.valores[self.ultimo_carro]
    else:
        return -1

def verificar_placa(self, placa):
    if self.rua_vazia():
        return False
    else:
        if placa in self.valores:
            for i in range(self.ultimo_carro + 1):
                if placa == self.valores[i]:
                    global posicao_carro
                    posicao_carro = i
                    break

            retirar_carros = self.ultimo_carro - posicao_carro
            print(f"Será preciso retirar {retirar_carros} carros para o veículo de placa {placa} sair!")

            return True
        else:
            return False


    
if __name__ == "__main__":
    c = Rua(7) 
    c.estacionar(765)
    c.estacionar(329)
    c.estacionar(907)

    print(c.verificar_placa(765))

