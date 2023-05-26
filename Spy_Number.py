n = int(input())
add, mul = 0, 1
for i in str(n):
    add += int(i)
    mul *= int(i)
y = add == mul
if y == True:
    print("Spy Number")
else:
    print("Not Spy Number")