n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    if(a+c) ==(b+d):
        print("YES")
    else:
        print("NO")