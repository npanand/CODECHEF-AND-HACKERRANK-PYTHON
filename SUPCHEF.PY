n=int(input())
while(0<n):
    a,b,c=map(int,input().split())
    
    if(a>b*c):
        print("yes")
    else:
        print("no")
    n=n-1