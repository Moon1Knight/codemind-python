s = input()

vowels = {'a', 'e', 'i', 'o', 'u'}

max_length = 0
current_length = 0

for char in s:
    if char in vowels:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0

print(max_length)
