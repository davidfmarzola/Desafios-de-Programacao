from itertools import product

def cartesian_product(A, B):
    return list(product(A, B))
A = input().split()
B = input().split()
A = [int(i) for i in A]
B = [int(i) for i in B]
result = cartesian_product(A, B)
# *o símbolo é usado para imprimir os elementos da lista em uma única linha com espaço
print(*result)