l = int(input())
n = list(map(int, input().split()))
c, k = 0, False
x, y, z = n[0], n[1], n[2]

while len(n) >= 3 and k == False:
    if n[0] < n[1] > n[2]:
        n = n[2:]
        c += 1
        
    else:
        n = n[2:]
        k = True
        break
    
if k == False:
    print(c)
else:
    print('-1')