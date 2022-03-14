n=int(input())
for i in range(n):
    x,m,n=map(int,input().split())
    c=(m*3) -(x-m)
    if c>=n:
        print("pass")
    else:
        print("fail")