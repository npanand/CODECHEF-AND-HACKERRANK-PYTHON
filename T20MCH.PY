# cook your dish here
r,o,c=map(int,input().split())
v=20-o
v=v*6*6
v=v+c
if(r>=v):
    print("no")
else:
    print("yes")