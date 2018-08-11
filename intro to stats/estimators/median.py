
def median(data):
    if len(data)%2 != 0:
        sdata = sorted(data)
        return sdata[(len(sdata)-1)//2]
    else:
        sdata = sorted(data)
        num = sdata[(len(sdata)//2)] + sdata[(len(sdata)-1)//2]
        return num/2
        
        
print (median([1,2,5,10,-20,10]))
