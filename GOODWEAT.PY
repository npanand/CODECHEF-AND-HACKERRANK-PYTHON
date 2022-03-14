n=int(input())
for i in range(n):
    f=0
    g=0
    a=map(int,input().split())
    for i in a:
        if(i==1):
            f=f+1
        elif(i==0):
            g=g+1
    if(f>g):
        print("YES")
    elif(g>f):
        print("NO")
    else:
        print("NO")