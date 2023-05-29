n = int(input())
x = list(map(int, input().split()))
c = sum(x)//(len(x))
y = c in x
print(y)