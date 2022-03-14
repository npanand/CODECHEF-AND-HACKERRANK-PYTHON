for i in range(int(input())):
    n=int(input())
    count=0
    for i in range(1,n+1):
        if(i%2==0):
            count=count-1
        else:
            count=count+3
    print(count)    