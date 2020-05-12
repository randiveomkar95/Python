"""
Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module.
"""
import calendar
draw = calendar.TextCalendar()
print(draw.formatmonth(2020, 5))
