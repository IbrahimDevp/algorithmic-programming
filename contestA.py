t = int(input())
while(t):
    ans =''
    n = int(input())
    a = list(input())
    total = int(a[0])
    for i in range(n-1):
        if total + int(a[i+1]) == 0:
            ans+='+'
            total += int(a[i+1])
            #print(total,int(a[i+1]),'1')
        elif total - int(a[i+1]) == 0:
            ans+='-'
            total -= int(a[i+1])
            #print(total,int(a[i+1]),'2')
        elif total + int(a[i+1]) == 1:
            ans+='+'
            total += int(a[i+1])
           # print(total,int(a[i+1]),'3')
        elif total - int(a[i+1]) == 1:
            ans+='-'
            total -= int(a[i+1])
            #print(total,int(a[i+1]),'4')
        else:
            ans+='-'
            total -= int(a[i+1])
        
        
    print(ans)
    t-=1
