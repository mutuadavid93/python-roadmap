# DATES don't exist natively instead are independent modules

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import calendar


##########################
#
#        DATES
#
##########################


# Current Date
today = date.today()

# Date Components:
print("Day: {} Month: {} Year: {}"
      .format(today.day, today.month, today.year))

# Week Day Number: i.e. index based
# week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Saturday", "Sunday"]
week_days = calendar.day_name
weekday = today.weekday()
print(f"Today is on a {week_days[weekday]}")

def print_date(message, date_object):
    print(f'{message} {date_object}')

def main():
    print_date("Today's date is", today)




##########################
#
#        TIME
#
##########################

# Get today's Date and Time
today_datetime = datetime.now()

# Get the current time
current_time = datetime.time(datetime.now())

# Get Time in UTC
# def utc_now():
#     now = datetime.utcnow()
#     return now

utc_now = lambda : datetime.utcnow()

print(utc_now())



##########################
#
#       TIME DELTA
#
##########################

# Calculates the span of time
basic_timedelta = timedelta(days=365, hours=5, minutes=1)

# Print today's date one year from now
one_year_from_now = str(datetime.now() + timedelta(days=365))

print("Today's date one year from now: %s"%(one_year_from_now))



if __name__ == '__main__': main()