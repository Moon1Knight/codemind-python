num = int(input())

is_prime_jhon = True
if num <= 1:
    is_prime_jhon = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime_jhon = False
            break

is_prime_javid = True
reverse_num = int(str(num)[::-1])
if reverse_num <= 1:
    is_prime_javid = False
else:
    for i in range(2, reverse_num):
        if reverse_num % i == 0:
            is_prime_javid = False
            break

if is_prime_jhon and is_prime_javid:
    print("circular prime")
elif is_prime_jhon:
    print("prime but not a circular prime")
else:
    print("not prime")
