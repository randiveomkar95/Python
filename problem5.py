"""
 Write a Python program to calculate the number of days between two dates.
 Sample dates : (2014, 7, 2), (2014, 7, 11) Expected output : 9 days
"""
from datetime import date

firstdate = date(2014, 7, 2)
lastdate = date(2014, 7, 11)

output = lastdate - firstdate
print(output.days)