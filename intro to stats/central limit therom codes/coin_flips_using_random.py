#function flip that simulates flipping n fair coins. 
#It returns a list representing the result of each flip as a 1 or 0
#To generate randomness,i have used the function random.random() to get
#a number between 0 or 1.

import random
from math import sqrt

def mean(data):
    return float(sum(data))/len(data)

def variance(data):
    mu=mean(data)
    return sum([(x-mu)**2 for x in data])/len(data)

def stddev(data):
    return sqrt(variance(data))
    

def flip(N):
    temp_list = []
    for x in range(N):
        if random.random() > 0.5:
            temp_list.append(1)     
        else:
            temp_list.append(0)
    return temp_list
    
N=1000
f=flip(N)
#print(f)

print (mean(f))
print (stddev(f))
