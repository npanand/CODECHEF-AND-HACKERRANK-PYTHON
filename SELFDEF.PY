n=int(input())
while(n>0):
    m=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in arr:
        if(10<=i<=60):
            count=count+1
    print(count)  