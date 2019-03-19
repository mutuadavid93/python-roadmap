# The Calendar Module:

import calendar

"""
    Print Text Calendar;
"""

c = calendar.TextCalendar(calendar.SUNDAY)
calendar_str = c.formatmonth(2019, 3, 0, 0)
print(calendar_str)

# Loop through Individual Month Days
# Zero means that days overlaps with another from a different month
for d in c.itermonthdays(2019,3):
    print(d)


# Get the Month and Day Names as they Appear in the Locale the
# computer is currently. e.g. Europe, China
for mnth in calendar.month_name:
    print("%s "%(mnth))


# Days too:
for dy in calendar.day_name:
    print("%s "%(dy))


"""
    A program to know the Date to the First Friday of the Month 
"""

# Months Start from 1 to 12:
for m in range(1,13):
    # Weeks in a Month: Returned as a List.
    weeks_in_month = calendar.monthcalendar(2019, m)

    # First Friday Must be Within the First two Weeks
    week_one = weeks_in_month[0]
    week_two = weeks_in_month[1]

    # Remember 0 means month's dates overlap
    if week_one[calendar.FRIDAY] != 0:
        meetday =  week_one[calendar.FRIDAY]
    else:
        meetday = week_two[calendar.FRIDAY]

    # %10s, means pad string by 10 spaces.
    print('%10s %2d'%(calendar.month_name[m], meetday))