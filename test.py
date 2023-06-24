from datetime import datetime

# getting the date time of now
now = datetime.now()
print(now)

# the data time of 2017
then = datetime(2017,5,20)
print(then)

# getting the differences from 5/20/2017 till date
difference_in_date = now - then
print(difference_in_date)

print(difference_in_date.days)  # outputs only the days
print(difference_in_date.seconds)  # outputs only the seconds




