n = int(input())
x = n*n
y = 0
for i in str(x):
    y += int(i)
    
if n == y:
    print("Neon Number")
else:
    print("Not Neon Number")