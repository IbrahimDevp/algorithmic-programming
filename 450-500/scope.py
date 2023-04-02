word = input()
word2 = []
box = []
count = 0
for i in range(len(word)):
    if word[i] == '(':
        word2.append(word[i])
        count=0
    elif word[i] in box:
        print('No')
        exit()
    elif word[i] == ')' and word[i-1] =='(':
        word2.pop()
    elif word[i]==')':
        word2.pop()
        if count!=0:
            del box[count*-1:]
            count=0
        else:
            box.clear()
    else:
        box.append(word[i])
        count+=1
print('Yes')
