def is_self_dividing(num):
    digits = []
    for digit in str(num):
        digits.append(int(digit))
    for digit in digits:
        if digit == 0 or num % digit != 0:
            return False
    return True

left = int(input())
right = int(input())

self_dividing_numbers = []
for num in range(left, right + 1):
    if is_self_dividing(num):
        self_dividing_numbers.append(num)

print(*self_dividing_numbers)
