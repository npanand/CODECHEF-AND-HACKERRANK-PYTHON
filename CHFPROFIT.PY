# cook your dish here
n=int(input())
for i  in range(n):
    a,b,c=map(int,input().split())
    h=a*b
    k=a*c
    v=k-h
    print(v)