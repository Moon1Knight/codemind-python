def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n1 = int(input())
n2 = int(input())

total_killed = n1 + n2

to_kill = 0
while True:
    total_killed += 1
    if is_prime(total_killed):
        break

to_kill = total_killed - (n1 + n2)

print(to_kill)
