hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

duraInHours = dura // 60
duraInMinutes = dura % 60

# extra hour if minutes go beyond 60
minuteBeyondHour = (duraInMinutes + mins) // 60
addedHour = minuteBeyondHour + duraInHours + hour

# minutes on clock



print(addedHour)
print()