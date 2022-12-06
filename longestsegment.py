import math
num = int(input())
arr1 = []
arr2 = []
result =0.0
for i in range (num):
    x,y = map(int,input().split())
    arr1.append(x)
    arr2.append(y)


for i in range(num):
    for j in range(num):
        result2 = math.sqrt(math.pow(arr1[j]-arr1[i],2)+math.pow(arr2[j]-arr2[i],2))
        if result2 > result: result = result2
print(result)