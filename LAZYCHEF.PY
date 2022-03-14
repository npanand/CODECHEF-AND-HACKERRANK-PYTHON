n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    f=min((a*b),(a+c))
    print(f)