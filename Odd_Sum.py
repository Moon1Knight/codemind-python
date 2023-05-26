n = int(input())
arr = list(map(int, input().split()))

sum_odd = 0

for i in range(n):
    if arr[i] % 2 != 0:
        sum_odd += arr[i]

print(sum_odd)
