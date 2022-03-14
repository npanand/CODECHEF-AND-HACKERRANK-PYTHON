# cook your dish here
for i in range(int(input())):
    n=int(input())
    if(n%4==0):
        print("North")
    elif(n%4==1):
        print("East")
    elif(n%4==2):
        print("South")
    else:
        print("West")
        
