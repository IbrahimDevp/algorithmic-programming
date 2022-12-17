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
            
           # print(total,int(a[i+1]),'5')
        
        #1-1 + 0 = 0
        #1-1 + 1 = 0

        #0-1 + 1 = 0
        #0-1 + 0 = -1

        #1+0 + 1 = 2
        #1+0 + 0 = 1

        #0-0 + 1 = 1
        #0+0 + 1 = 1
        #0+0 + 0 = 0
        # if a[i]== '0' and a[i+1]== '0':
        #     ans+='+'
        # elif a[i]== '1' and a[i+1]== '0':
        #     ans+='+'
        #     total +=1
        # elif a[i]== '0' and a[i+1]== '1':
        #     print(total)
        #     if total > 0:
        #         ans+='-'
        #         total -=1
        #     else:
        #         ans+='+'
        #         total +=1
        # elif a[i]=='1' and a[i+1]=='1':
        #     ans+='-'
        # else:
        #     ans+='not'
        
        
    print(ans)
    t-=1
