from collections import OrderedDict
n = int(input())
my_words = OrderedDict()

for i in range(n):
    word = input()
    if word not in my_words:
        my_words[word] = 1
    else: my_words[word] +=1
    
print(len(my_words))
for v in my_words.values():
    print(v, end=' ')
    
