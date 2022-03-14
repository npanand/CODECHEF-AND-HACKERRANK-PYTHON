# cook your dish here
n=int(input())
while(n>0):
    
    a,b,c,d,e=map(int,input().split())
    f=a-b
    g=c+d+e
    if(f>=g):
        print("YES")
    else:
        print("NO")
    
    n=n-1