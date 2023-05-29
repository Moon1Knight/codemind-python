n = int(input())
x = list(map(int, input().split()))
eve = []
for i in x:
    if i%2 == 0:
        eve.append(i)
        
print(eve[-1])