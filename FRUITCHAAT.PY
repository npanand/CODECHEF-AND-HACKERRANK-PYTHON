n=int(input())
while(0<n):
    a,b=map(int,input().split())
    c=a//2
    f=min(c,b)
    print(f)
    n=n-1