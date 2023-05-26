num = int(input())
x =  int(str(num)[::-1]) if num >= 0 else -int(str(abs(num))[::-1])
print(x)