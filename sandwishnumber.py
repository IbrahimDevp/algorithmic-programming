word = list(input())
s1 = ''
s2 = ''
num = ''
visited = False
for i in range(len(word)):
    if  'A'<= word[i] <= 'Z' and visited==False:
        s1 += word[i]
        if(len(s1)>1):
            print('No')
            exit()
    if '0'<=word[i] <= '9':
        num+=word[i]
        if(len(num)>6):
            print('No')
            exit()
        visited = True
    if  'A'<= word[i] <= 'Z' and visited==True:
        s2 +=word[i]
        
        if(len(s2)>1):
            print('No')
            exit()
if len(num) < 6 or len(s1) < 1 or len(s2) < 1:
    print('No')
    exit()
anum = int(num)
if 'A'<= s1 <= 'Z' and 100000 <= anum <= 999999 and 'A'<= s2 <= 'Z':
    print('Yes')
else:
    print('No')
