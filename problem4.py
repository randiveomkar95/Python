"""
Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module.
Resource : https://www.w3resource.com/python/module/calendar/text-calendar-formatmonth.php
"""
import calendar
draw= calendar.TextCalendar()
print(draw.formatmonth(2020, 5))
