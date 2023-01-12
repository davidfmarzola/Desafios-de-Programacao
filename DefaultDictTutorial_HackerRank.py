from collections import defaultdict

n,m = map(int,input().split())
a,b=defaultdict(list),[]
for i in range(n): a[input()].append(i+1) 
for i in range(m): b.append(input())

for i in range(m): 
    if(a[b[i]]):
        print(' '.join(map(str,a[b[i]])))
    else: print("-1")