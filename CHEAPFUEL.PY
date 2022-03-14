
for i in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    petrol=(a+e*c)
    diesel=(b+e*d)
    
    if(petrol>diesel):
        print("DIESEL")
    elif(petrol<diesel):
        print("PETROL")
    else:
        print("SAME PRICE")