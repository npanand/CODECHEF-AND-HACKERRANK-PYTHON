for i in range(int(input())):
    a,a1,b,b1,c,c1,d,d1,e,e1=map(int,input().split())
    k=a+b+c+d+e
    l=a1+b1+c1+d1+e1
    if(k>l):
        print("1")
    elif(l>k):
        print("2")
    else:
        print("0")