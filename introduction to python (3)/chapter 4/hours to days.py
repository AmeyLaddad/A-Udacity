def hours2days(hours):
    days = hours // 24
    hour = hours % 24
    return (days,hour)
    
    
print (hours2days(28))