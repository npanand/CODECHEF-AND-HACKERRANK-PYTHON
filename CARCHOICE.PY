n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    car1=c/a
    car2=d/b
    if(car1<car2):
        print("-1")
    elif(car1==car2):
        print("0")
    else:
        print("1")