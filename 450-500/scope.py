word = input()
word2 = []
box = []
flag = True
for i in range(len(word)):
    if word[i] == '(':
        word2.append(word[i])
    elif word[i]==')':
        while(True):
            tmp = word2.pop()
            if tmp =='(':
                break
            else:
                box.remove(tmp)
    else:
        if word[i] in box:
            flag = False
            break
        else:
            word2.append(word[i])
            box.append(word[i])
if flag == False:
    print('No')
else:
    print('Yes')