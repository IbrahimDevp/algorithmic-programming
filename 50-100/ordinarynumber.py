n = int(input())
arr = list(map(int,input().split()))
ordnum = list()
for i in range(1,n,2):
    templist = []
    temp1= max (arr[i],arr[i+1],arr[i-1])
    temp2= min (arr[i],arr[i+1],arr[i-1])
    
        ordnum.append(arr[i])
print(len(set(ordnum)))