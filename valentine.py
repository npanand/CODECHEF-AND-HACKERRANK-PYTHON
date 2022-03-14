n=int(input())
for i in range(n):
    m,n=map(int,input().split())
    if m>n:
        b=m//n
        print(b)
    else:
        print(m//n)