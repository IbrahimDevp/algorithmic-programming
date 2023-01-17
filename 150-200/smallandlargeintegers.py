A,B,K = map(int,input().split())
list1 = list()
size = B - A + 1
while(K != 0 and size !=0):
    list1.append(A)
    list1.append(B)
    A+=1
    B-=1
    K-=1
    size-=1
nlist = sorted(list(set(list1)))

print(*nlist, sep ="\n")