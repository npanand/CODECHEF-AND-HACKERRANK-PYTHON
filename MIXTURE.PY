# cook your dish here
n=int(input())
f=0
g=0
for i in range(n):
    a,b=map(int,input().split())
    if(a>0)and (b>0):
        print("Solution")
    elif(a==0) or (b>0):
        if(a==0):
            print("Liquid")
    elif(a>0) or (b == 0):
        if(b==0):
            print("Solid")