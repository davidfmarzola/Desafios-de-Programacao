def count_substring(string, sub_string):
    # times sub_string occurs
    occurrences = 0

    # last found index of sub_string
    j = 0
    for i in range(len(string)):
        # if j = -1 the whole word has already been scrollen through
        while(j != -1):
            j = string.find(sub_string, j, len(string))
            if j >= 0:
                occurrences += 1
                j += 1

    return occurrences

# finding the amount of substring in a string
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)