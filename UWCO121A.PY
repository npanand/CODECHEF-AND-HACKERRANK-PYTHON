import math
t = int(input())
for i in range(t):
    n = int(input())

    for i in range(1, n+1):

            if n%i == 0:
                print(i, "\t", math.floor(n/i))

                break;