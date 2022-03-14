n=int(input())
d=[]
for i in range(10,0,-1):
    if(n%i==0):
        d.append(i)
 
print(max(d))