t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]==-1:
            a[i]=1
            break
        elif a[i]==1:
            break
    for i in range(n-1,-1,-1):
        if a[i]==-1:
            a[i]=1
            break
        elif a[i]==1:
            break
    for i in range(n):
        if a[i]==-1:
            a[i]=0
    for x in a:
        print(x,end=" ")


