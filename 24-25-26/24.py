# import datetime
# from time import strftime
#
# datetime.date(2015, 6, 16)
# print(strftime("%V"))

########################################

# import time
# print(time.asctime(time.strptime('2015 50', '%Y %W')))

####################################################

# from datetime import date, timedelta
#
#
# def all_sundays(year):
#     # January 1st of the given year
#     dt = date(year, 1, 1)
#     # First Sunday of the given year
#     dt += timedelta(days=6 - dt.weekday())
#     while dt.year == year:
#         yield dt
#         dt += timedelta(days=7)
#
#
# for s in all_sundays(2020):
#     print(s)


###############################################

# import datetime
# from datetime import date
# def addYears(d, years):
#     try:
# #Return same day of the current year
#         return d.replace(year = d.year + years)
#     except ValueError:
# #If not same day, it will return other, i.e.  February 29 to March 1 etc.
#         return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))
#
# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29),1))