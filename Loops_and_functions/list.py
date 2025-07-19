# Class excersizes

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekday)

weekday[2] = 'Humpday'
print(weekday)

del weekday[3]
print(weekday)

merged = weekday[1] + '-' + weekday[2]
weekday[1] = merged
del weekday[2]
print(weekday)

