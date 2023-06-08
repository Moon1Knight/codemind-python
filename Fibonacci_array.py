n = int(input())
x = list(map(int, input().split()))
c = 0
while len(x) > 2:
    a, b, c = x[0], x[1], x[2]
    if a + b == c:
        x = x[1:]
        c = 1
        
    else:
        c = 0
        break
    
if c == 0:
    print("no")
else:
    print("yes")