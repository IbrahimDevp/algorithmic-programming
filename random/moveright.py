string = str(input())
list1 = list(string)
for i in range(len(string)-1,-1,-1):
    if (i == 0):
        list1[i]='0'
    else:
        list1[i] = list1[i-1]
str1 = ''.join(list1)
print(str1)