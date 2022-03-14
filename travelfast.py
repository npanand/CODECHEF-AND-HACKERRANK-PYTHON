n=int(input())
for i in range(n):
    bike,car =  map(int,input().split())
    if bike < car :
        print("BIKE")
    elif(car == bike):
        print("SAME")
    else:
        print("CAR")