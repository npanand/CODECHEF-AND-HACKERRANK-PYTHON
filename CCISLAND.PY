n=int(input())
for _ in range(n):
    a,b,c,d,e=map(int,input().split())
    
    print("YES" if c*e<=a and d*e<=b  else "NO")