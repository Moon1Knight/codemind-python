n = int(input())
x = n ** 2
a, b = str(n), str(x)
if b.endswith(a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")