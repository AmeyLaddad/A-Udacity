
def mean(data):
    return sum(data)/len(data)
def variance(data):
    m = mean(data)
    list_temp = []
    for x in data:
        diff = x - m
        list_temp.append(diff*diff)
    return mean(list_temp)
        
print (variance([13.04, 1.32, 22.65, 17.44, 29.54, 23.22, 17.65, 10.12, 26.73, 16.43]))
