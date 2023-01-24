n = int(input())
s = set(map(int, input().split()))
c = int(input())

for i in range(c):
    entrada = input().split()
    if entrada[0] == 'pop': 
        s.pop()
    elif entrada[0] == 'remove': 
        s.remove(int(entrada[1]))
    else: 
        s.discard(int(entrada[1]))
print(sum(s))