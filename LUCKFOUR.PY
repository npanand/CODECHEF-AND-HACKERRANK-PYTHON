n=int(input())
for i in range(n):
    h=int(input())
    d=str(h)
    c=0
    for i in range(len(d)) :
        f=h%10
        h=h//10
        if(f == 4):
            c=c+1
    print(c)