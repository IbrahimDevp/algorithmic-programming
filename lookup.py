s = str(input())
t = str(input())

for i in range(len(s)):
    if s[i] == t[0]:
        if s[i:len(t)+i] == t:
            print('Yes')
            exit()
print('No')
