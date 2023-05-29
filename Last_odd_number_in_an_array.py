n = int(input())
x = list(map(int, input().split()))
odd = []
for i in x:
    if i%2 != 0:
        odd.append(i)
print(odd[-1])