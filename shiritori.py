N = int(input())
W = list()
flag = False
for i in range(0,N):
    word = input()
    if i > 0 :
        word2 = W[i-1]
        if word in W  or word2[-1] != word[0]:
            flag = True
    W.append(word)
    
if flag == True:
    print('No')
else:
    print('Yes')