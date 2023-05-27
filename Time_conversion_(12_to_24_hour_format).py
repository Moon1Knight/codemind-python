time_12h = input() 
hours, minutes, period = time_12h.split(":")[0], time_12h.split(":")[1][:2], time_12h.split()[-1]
hours = int(hours)

if period == "AM" and hours == 12:
    hours = 0
elif period == "PM" and hours < 12:
    hours += 12

time = f"{hours:02d}:{minutes}"
print(time)