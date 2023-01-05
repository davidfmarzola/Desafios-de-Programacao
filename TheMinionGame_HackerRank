 
def check_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    # pego a primeira vogal que ocorre na string e sua posicao
    vowels_list = [first for first in string if first in vowels]
    first_vowel = vowels_list[0] 
    start = string.find(vowels_list[0])
    count = 0
    i = len(string)
    for i in range(i, start, -1):
        sub_string = string[start:i]
        count = string.count(sub_string)
        print(sub_string)
        print(count)
def minion_game(string):      
    check_vowels(string)

if __name__ == '__main__':
    s = input()
    minion_game(s)
