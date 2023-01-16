A,B = map(int, input().split())
C = list(str(A))

count = 0
for i in range(A,B+1):
    T1 = list(str(i))
    T1.reverse()
    T2 = str(T1)
    T1.reverse()
    if T2 == str(T1):
        count+=1
print(count)
