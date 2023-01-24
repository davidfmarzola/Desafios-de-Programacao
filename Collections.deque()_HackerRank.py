from collections import deque
n = int(input())
d = deque()

for i in range(n):
    array = input().split()
    if array[0] == "append":
        d.append(array[1])
    elif array[0] == "appendleft":
        d.appendleft(array[1])
    elif array[0] == "pop":
            d.pop()
    else:
        d.popleft()
        
print(" ".join(d))
