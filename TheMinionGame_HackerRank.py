def start_position_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    # pego a primeira vogal que ocorre na string e sua posicao
    vowels_list = [first for first in string if first in vowels]
    start = string.find(vowels_list[0])
    return start

def count_number_of_vowels(sub_string_list, string):
    count_v = 0
    start = start_position_vowels(string)
    for i in range(len(sub_string_list)):
        j=start
        # verifica se a sub_string existe na string no intervalo[j, len(string)]
        while j!=-1:
            j = string.find(sub_string_list[i], j, len(string))
            if j >= 0:
                count_v += 1
                j += 1
    return count_v
 
def identify_vowels(string):
    start = start_position_vowels(string)
    sub_string_list = []
    i = len(string)
    for i in range(i, start, -1):
        sub_string = string[start:i]
        sub_string_list.append(sub_string)
    return sub_string_list

def find_string_consonants(string):
    from collections import OrderedDict  
    consonants = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    consonants_list = [first for first in string if first in consonants]
    consonants_list = list(OrderedDict.fromkeys(consonants_list)) # removendo duplicatas
    return consonants_list
    
def identify_consonants(string):
    string_consonants = find_string_consonants(string)
    sub_string_list = []
    for i in range(len(string_consonants)):
        start = string.find(string_consonants[i])
        j = len(string)    
        for j in range(j, start, -1):
            sub_string = string[start:j]
            sub_string_list.append(sub_string)
    return sub_string_list

def count_number_of_consonants(sub_string_list, string):
    count_c = 0
    c=0
    string_consonants = find_string_consonants(string)
    for k in range(len(string_consonants)):
        start = string.find(string_consonants[k])
        # como pegar a primeira letra de cada string em um vetor de strings?
        #c=0
        for d in range(len(sub_string_list)):
            if sub_string_list[d].startswith(string_consonants[k]):
                c+=1
        for i in range(c):
            j=start
            # verifica se a sub_string existe na string no intervalo[j, len(string)]
            while j!=-1:
                j = string.find(sub_string_list[i], j, len(string))
                if j >= 0:
                    #print(sub_string_list[i])
                    #print(j)
                    count_c += 1
                    j += 1
    return count_c

def minion_game(string):   
    kevin_score = count_number_of_vowels(identify_vowels(string), string)
    stuart_score = count_number_of_consonants(identify_consonants(string), string)
    if kevin_score > stuart_score:
        print('Kevin', kevin_score)
    elif kevin_score < stuart_score:
        print('Stuart', stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)