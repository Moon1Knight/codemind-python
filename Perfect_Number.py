def is_perfect_number(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

n = int(input())
is_perfect = is_perfect_number(n)
print(is_perfect)
