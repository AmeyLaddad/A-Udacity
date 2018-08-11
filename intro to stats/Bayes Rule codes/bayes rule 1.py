#Return the probability of A conditioned on B given that 
#P(A)=p0, P(B|A)=p1, and P(Not B|Not A)=p2 

def f(p0,p1,p2):
    norm = p0*p1 + (1-p0)*(1-p2)
    return p0*p1/norm

