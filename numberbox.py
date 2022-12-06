num = int(input())

list1 = [[] for _ in range (num)]
max = 0
for i in range (num):
    a = input()
    list1[i] = a
max = []
locnum = 1000
loc = []
for _ in range (num):
    maxnum = 0
    for i in range(0,num):
        for j in range(0,num):
            if(maxnum < int(list1[i][j])):
                    locnum1 = str(i)+str(j)
                    print(maxnum)
                    if (locnum1 not in loc):
                        maxnum = int(list1[i][j])
                        locnum = int(locnum1)
    loc.append(locnum)
    max.append(maxnum)
print(loc)
print(max)