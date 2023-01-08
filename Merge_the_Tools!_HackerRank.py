def merge_the_tools(string, k):
    # 1. armazeno as substrings em uma lista
    substring = []
    i = 0 
    j = k
    while j <= len(string):
        substring.append(string[i:j])
        i+=k
        j+=k
    # 2. removo o caractere repetido de cada string
    for i in range(len(substring)):
        substring[i] = ''.join(list(dict.fromkeys(list(substring[i]))))
        print(substring[i])
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)