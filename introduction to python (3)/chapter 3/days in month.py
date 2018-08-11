def how_many_days(month_number):
    """Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = days_in_month[month_number-1]
    #todo: return the correct value
    return month
print(how_many_days(8))
