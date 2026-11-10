time_24 = input("Enter time (24-hour format): ")
hours, minutes = map(int, time_24.split(":"))

period = "am" if hours < 12 else "pm"
hours_12 = hours % 12
if hours_12 == 0:
    hours_12 = 12

print(f"Time in 12-hour format: {hours_12}:{minutes:02d}{period}")
