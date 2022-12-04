list1 = []
len = int(input())
for i in range (0,len):
    list1.append([])
for i in range (0,len):
    for j in range (0,len):
        list1[i].append(j)
        list1[i][j]=''
for i in range (0,len):
    for j in range (0,len):
        list1[i][j] = str(input())
for i in range (0,len):
    for j in range (0,len):
        if i==j:
            if list1[i][j]!='-':
                print('incorrect')
                exit()
        else:
            if list1[i][j] == 'W':
                if list1[j][i] != 'L':
                    print('incorrect')
                    exit()
            elif list1[i][j] == 'L':
                if list1[j][i] != 'W':
                    print('incorrect')
                    exit()
            elif list1[i][j] == 'D':
                if list1[j][i] != 'D':
                    print('incorrect')
                    exit()
            else:
                print('incorrect')
                exit()
print('correct')