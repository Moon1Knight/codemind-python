n = int(input())
x = list(map(int, input().split()))
eve = [i for i in x if i%2==0]
print(eve[-1])