from math import sqrt

def mean(l):
    return float(sum(l))/len(l)

def var(l):
    m = mean(l)
    return sum([(x-m)**2 for x in l])/len(l)

def factor(l):
    return 1.96 # Assssumption !!! Not always true for smaller size sample set


def conf(l):
    return factor(l) * sqrt(var(l) / len(l))

l = [199,200,201,202,203,204]
h = 202

def test(l, h):
    m = mean(l)
    c_i = conf(l)
    return abs(h-m) <= c_i
    
print (conf(l))
print (mean(l))
print (test(l,h))