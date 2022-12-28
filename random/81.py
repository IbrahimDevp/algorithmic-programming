number = int(input())
for i in range (1,10):
    for j in range (1,10):
        if (i*j == number):
            print('Yes')
            exit()
print('No')