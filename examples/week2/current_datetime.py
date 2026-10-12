from datetime import datetime
print("Current Date Time Example Program")

# Get the current datetime
current_datetime = datetime.now()

# Print in standard and formatted output
print("Current date and time:", current_datetime)

print("Current date:", current_datetime.strftime("%m/%d/%Y"))
print("Current time:", current_datetime.strftime("%I:%M %p"))
