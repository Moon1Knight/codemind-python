n =int(input())
x = list(map(int, input().split()))
a, c = int(input()), 0
for i in x:
    if i == a:
        c += 1
        
print(c)
