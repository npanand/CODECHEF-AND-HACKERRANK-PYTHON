n=int(input())
while(n>0):
    a,b,c,d=map(int,input().split())
    f=c//a
    e=d//b
    print(int(f)+int(e))

    n=n-1 