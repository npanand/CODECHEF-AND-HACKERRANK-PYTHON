for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    f=(((b+c//2))*a)
    if(f<=d):
        print("YES")
    else:
        print("NO")
