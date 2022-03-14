n=int(input())
for i in range(n):
    m,n=map(int,input().split())
    c=21-(m+n)
    if 1<= c and c <=10 :
        print(c)
    else:
        print(-1)