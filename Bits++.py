c = 0
for _ in range(int(input())):
    x = input()
    if '+' in x:
        c += 1
    elif '-' in x:
        c -= 1
print(c)