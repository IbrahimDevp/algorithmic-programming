N,A,B=map(int,input().split())

count = N//(A+B)
A_count = count * A
rem = N%(A+B)

ans = A_count + min(rem,A)
print(ans)