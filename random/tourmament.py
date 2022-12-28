
len = int(input())


list1 = [[] for _ in range(len)]

for i in range(len):
    a = input()
    list1[i] = a

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