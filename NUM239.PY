n=int(input())

for _ in range(n):
    a,b=map(int,input().split())
    count=0
    for i in range(int(a),int(b)+1,1):
        
        f=[2,3,9]
        c=i%10
        if c in f:
            count=count+1
    print(count) 

