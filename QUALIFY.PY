n=int(input())
for i in range(n):
    x, a,b=map(int,input().split())
    p=(a*1+b*2)
    print("Qualify"   if(p>=x) else "NotQualify "  )