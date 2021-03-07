hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins = mins + dura  # finds updated mins after duration
hour = hour + mins // 60  # finds the extra hours from updated mins to add to hour
mins = mins % 60  # extra mins beyond the hour to be find in updated mins
hour = hour % 24  # remainder left over,

print(hour, ":", mins, sep='')
