s = input()
string=[]
digits = []
upper=[]
for i in range(len(s)):
    if s[i]>='0' and s[i]<='9':
        digits.append(s[i])
    elif s[i]>='a' and s[i]<='z':
        string.append(s[i])
    else:
        upper.append(s[i])
string = sorted(string)
upper = sorted(upper)
strupper = ''
for l in upper:
    strupper += l
string.append(strupper)
odddigits = []
evendigits=[]
for i in range(len(digits)):
    digits[i] = int(digits[i])
    if(digits[i]%2==0):
        odddigits.append(digits[i])
    else:
        evendigits.append(digits[i])

odddigits=sorted(odddigits)
evendigits=sorted(evendigits)
digitsordered = string+evendigits+odddigits
for i in digitsordered:
    print(i, end='')