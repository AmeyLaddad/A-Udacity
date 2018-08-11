#Given that the probability of one head is p, return the probability of
#two flips resulting in two heads

def f1(p):
    return p*p  



#Return the probability of exactly one head in three flips

def f2(p):
    return p*(1-p)*(1-p)*3
    
    

#Return the probability of flipping one head each from two coins
#One coin has a probability of heads of p1 and the other of p2

def f3(p1,p2):
    return p1*p2



#Two coins have probabilities of heads of p1 andd p2
#The probability of selecting the first coin is p0
#Return the probability of a flip landing on heads

def f4(p0,p1,p2):
    ans = (p0*p1)+(1-p0)*p2
    return ans 
  
    
   
