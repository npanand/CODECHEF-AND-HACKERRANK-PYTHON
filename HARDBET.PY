# cook your dish here
n=int(input())
while(n>0):
    a,b,c=map(int,input().split())
    if(c<a) and (c<b):
        print("ALICE")
    elif(b<a)and(b<c):
        print("BOB")
    else:
        print("DRAW")
    n=n-1