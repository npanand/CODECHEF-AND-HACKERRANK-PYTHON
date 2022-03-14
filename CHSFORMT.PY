# cook your dish here
n=int(input())
while(n>0):
    a,b=map(int,input().split())
    c=a+b
    if(c<3):
        print("1")
    elif( 3<= c <=10):
        print("2")
    elif(11<= c <=60):
        print("3")
    elif(60<c):
        print("4")
        
    
    n=n-1
    
