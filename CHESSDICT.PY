n=int(input())
while(n>0):
    x1,y1,x2,y2=map(int,input().split())
    j=max(abs(x1-x2),abs(y1-y2))
    print(j)
    n=n-1
