def start_position_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    # pego a primeira vogal que ocorre na string e sua posicao
    vowels_list = [first for first in string if first in vowels]
    start = string.find(vowels_list[0])
    return start

def count_number_of_vowels(sub_string_list, string):
    count = 0
    start = start_position_vowels(string)
    for i in range(len(sub_string_list)):
        j=start
        # verifica se a sub_string existe na string no intervalo[j, len(string)]
        while j!=-1:
            j = string.find(sub_string_list[i], j, len(string))
            if j >= 0:
                count += 1
                j += 1
    return count
 
def identify_vowels(string):
    start = start_position_vowels(string)
    sub_string_list = []
    i = len(string)
    for i in range(i, start, -1):
        sub_string = string[start:i]
        sub_string_list.append(sub_string)
    return sub_string_list

def minion_game(string):      
    count_number_of_vowels(identify_vowels(string), string)

if __name__ == '__main__':
    s = input()
    minion_game(s)