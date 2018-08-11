def mode(data):
    count_mode = 0
    for x in range(len(data)):
        xcount = data.count(data[x])
        if xcount > count_mode:
            ans = data[x]
            count_mode = xcount 
            
    return ans


data1=[1,2,5,10,-20,5,5]
