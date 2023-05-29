n = int(input())
x = list(map(int, input().split()))
c = -1
for i in range(n):
    if x[i]%2 != 0:
        c = i
print(c)