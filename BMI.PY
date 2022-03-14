n=int(input())
while (n>0):
    m,h=map(int,input().split())
    f=m//(h**2)
    if(f<=18):
        print("1")
    elif(19<= f <=24):
        print("2")
    elif(25<= f <= 29):
        print("3")
    elif(f>=30):
        print("4")
        
    n=n-1