def readable_timedelta(days):
    """ This is a function that returns input days number in weeks and days format"""
    Weeks = days // 7
    Days = days % 7
    
    return ("{} week(s) and {} days".format(Weeks,Days))
    
print (readable_timedelta(9))