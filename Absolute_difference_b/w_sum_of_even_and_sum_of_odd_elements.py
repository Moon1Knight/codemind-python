n = int(input())
arr = list(map(int, input().split()))

sum_even = 0
sum_odd = 0

for i in range(n):
    if arr[i] % 2 == 0:
        sum_even += arr[i]
    else:
        sum_odd += arr[i]

abs_diff = abs(sum_even - sum_odd)
print(abs_diff)
