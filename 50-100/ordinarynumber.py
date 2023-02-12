n = int(input())
arr = list(map(int,input().split()))
ordnum = list()
for i in range(1,n-1):
    arr2 = [arr[i-1],arr[i],arr[i+1]]
    arr2.sort()
    ordnum.append(arr2[1])
print(len(set(ordnum)))