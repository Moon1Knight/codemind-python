p, r, t = map(float, input().split())
amount = p*(1+r/100)**t
formatted_amount = "{:.2f}".format(amount)

print(formatted_amount)