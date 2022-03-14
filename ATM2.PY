n=int(input())
for i in range(n):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    
    for i in arr:
        if(i<=k):
            print("1",end="")
            k=k-i
        else:
            print("0",end="")
    print()  