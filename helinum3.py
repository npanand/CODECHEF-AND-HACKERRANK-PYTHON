n=int(input())
for i in range(n):
    j=list(map(int,input().split()))
    if j[2]*j[3]>=j[0]*j[1]:
        print("yes")
    else:
        print("no")