n = input()

x = ' '
for i in range(len(n)-1, -1, -1):
    x += n[i]
    
print(int(x))
    