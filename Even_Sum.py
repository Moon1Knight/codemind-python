n = int(input())
arr = list(map(int, input().split()))

sum_even = 0

for i in range(n):
    if arr[i] % 2 == 0:
        sum_even += arr[i]

print(sum_even)
