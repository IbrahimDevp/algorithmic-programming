word = input()
a = word[0]+word[-1]

if len(word) ==8 and a.isupper() and a.isalpha() and word[1:-1].isnumeric() and int(word[1]) > 0:
    print('Yes')
else:
    print('No')
