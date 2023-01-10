# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
lista = map(int, input().split())
lista = Counter(lista)
N = int(input())
total_money = 0
for i in range(N):
    shoes_size_desired, price = map(int, input().split())
    if lista[shoes_size_desired] > 0:
        total_money += price
        lista[shoes_size_desired] -= 1
        
print(total_money)
        