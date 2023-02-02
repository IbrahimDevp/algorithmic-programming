K = int(input())
A,B = map(str,input().split())
a,b=0,0
for i in range(len(A)-1,-1,-1):
    a+= int(A[abs(len(A)-1-i)])*K**i
for i in range(len(B)-1,-1,-1):
    b+= int(B[abs(len(B)-1-i)])*K**i
print(a*b)