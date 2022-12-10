h,m = map(int,input().split())

if h < 10:
    AC ='0'+str(h)
else: AC = str(h)
if m < 10:
    BD = '0'+str(m)
else: BD = str(m)

check = True
ans = ''
nAC = int(AC[0]+BD[0])
nBD = int(AC[1]+BD[1])
while(check):
    nAC = int(AC[0]+BD[0])
    nBD = int(AC[1]+BD[1])
    #print(nAC,nBD)
    if nAC>23 or nBD>59:
        m += 1
        if m < 10:
            BD = '0'+str(m)
        elif m == 60:
            m = 0
            BD = '00'
            h += 1
            if h>23:
                h = 0
                AC = '00'
            elif h<10:
                AC ='0'+str(h)
            else:
                AC =str(h)
        else:
            BD = str(m)
    else:
        print(int(AC),int(BD))
        check = False

