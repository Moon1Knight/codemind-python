n = int(input())
while n>9:
    k = str(n)
    d = sum(int(i) for i in k)
    n = d
    
r = n
print(r)