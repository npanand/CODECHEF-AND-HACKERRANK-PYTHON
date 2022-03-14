# cook your dish here
n=int(input())
for i in range(n):
    n=int(input())
    if(1<=n<100):
        print("easy".upper())
    elif(100<= n <200):
        print("medium".upper())
    elif(200<= n <=300):
        print("hard".upper())