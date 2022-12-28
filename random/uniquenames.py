num = int(input())

names=[[[],[]] for _ in range(num)]
for i in range (0,num):
    a = str(input())
    names[i]=a.split()

flag1,flag2 = 0,0
for i in range(num):
    for j in range(num):
        if (i!=j):
            if names[i][0] == names[j][0] or names[i][0] == names[j][1]:
                flag1 = 1
            if names[i][1] == names[j][0] or names[i][1] == names[j][1]:
                flag2 = 1
    if (flag1== 1 and flag2 == 1):
        print('No')
        exit()
print('Yes')