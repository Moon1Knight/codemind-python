def is_pronic_number(num):
    for i in range(1, int(num/2) + 1):
        if i * (i + 1) == num:
            return "YES"
    return "NO"

num = int(input())
result = is_pronic_number(num)
print(result)
