n = int(input())
high, low = 1, 0
while low < n:
    prev = low
    low = high
    high += prev
    
if (n - prev) <(low -n):
    print(prev)
elif (n - prev) > (low - n):
    print(low)
else:
    print(prev, low)
    
