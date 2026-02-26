#1️ Subtract five days from current date
from datetime import datetime, timedelta

# Get current date and time
current_date = datetime.now()

# Subtract 5 days using timedelta
new_date = current_date - timedelta(days=5)

# Print results
print("Current date:", current_date)
print("Five days ago:", new_date)



#2 Print yesterday, today, tomorrow
from datetime import datetime, timedelta

# Get today's date (without time)
today = datetime.now().date()

# Calculate yesterday and tomorrow
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

# Print all dates
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)



#3 Drop microseconds from datetime
from datetime import datetime

# Get current datetime with microseconds
current_datetime = datetime.now()

# Remove microseconds using replace()
without_microseconds = current_datetime.replace(microsecond=0)

# Print before and after
print("Before:", current_datetime)
print("After:", without_microseconds)


#4 Calculate difference between two dates in seconds
from datetime import datetime

# Define two datetime values
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 25, 15, 30, 0)

# Subtract to get timedelta
difference = date2 - date1

# Convert timedelta to seconds
seconds = difference.total_seconds()

# Print result
print("Difference in seconds:", seconds)