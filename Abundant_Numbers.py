n = int(input())
prop_fac = []
for i in range(1, n):
    if n%i == 0:
        prop_fac.append(i)
if sum(prop_fac) > n:
    print(True)
else:
    print(False)