n = input()
h, m = n.split(':')
h = int(h)
if h<12:
    p = "AM"
else:
    p = "PM"
if h == 0:
    h = 12
elif h >12:
    h -= 12
print(f"{h:02d}:{m} {p}")