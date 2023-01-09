# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

S, k = input().split()
lista = list(permutations(S, int(k)))
result = []
for i in range(len(lista)):
    result.append(''.join(lista[i]))

result = sorted(result)
print(*result, sep='\n')