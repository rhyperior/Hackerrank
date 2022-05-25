"""
The calendar module allows you to output calendars and provides additional useful functions for them.

class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY   format.

Constraints
2000 < YEAR < 3000

Output Format
08 05 2015

"""
import calendar
if __name__=="__main__":
    # d = c.formatweekheader(5)
    month, date, year = map(int, input().split())
    e = calendar.weekday(2022, 5, 25)
    d = calendar.TextCalendar().formatweekday(e, 10).strip().upper()
    print(d)