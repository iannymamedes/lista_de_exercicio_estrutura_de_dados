# Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.


def pilhas_iguais(pilha1:list,pilha2:list):
    if pilha1 == pilha2:
        return True
    else:
        return False

x = pilhas_iguais([1,2,3,4,5],[1,2,3,4,5])
z = pilhas_iguais([9,8,7,6,5],[5,6,7,8,9])
print(x)
print(z)