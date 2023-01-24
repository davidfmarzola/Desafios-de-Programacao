m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))

lis = list(a.difference(b)) + list(b.difference(a))
print(*sorted(lis), sep='\n')
