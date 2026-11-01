t=int(input())
res=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    l=[0]*4
    for x in a:
        if x%2:
            if x%4:
                l[0]+=1
            else:
                l[1]+=1
        else:
            if x%4:
                l[2]+=1
            else:
                l[3]+=1
    res.append(max(l))
for x in res:
    print(x)