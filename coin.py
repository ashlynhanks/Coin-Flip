#__author__ = "Ashlyn Hanks"
#__copyright__ = "Copyright 2020"
#__credits__ = []
#__license__ = "GPLv3"
#__version__ = "0.0.0"
#__maintainer__ = "Ashlyn Hanks"
#__email__ = "ahanks@highpoint.edu"
#__status__ = "Development"
import numpy as np

probability = .5
#num of flips required. This can be changed.
n = input("How many times would you like to flip a coin?\n")
n = int(n)
h = input("How many times would you like to fip heads?\n")
h = int(h)
# n = flips, h = heads, t = tails
t = n - h

p = (h/t)*100
roundp = round(p,2)
hc = 0
tc = 0

fullResults = np.arange(n)
def coinFlip(p):    
    #perform the binomial distribution (returns 0 or 1)    
    result = np.random.binomial(1,p) 
       
    #return flip to be added to numpy array    
    return result


for i in range(0, n):    
    fullResults[i] = coinFlip(probability)    
    i+=1

#print results
print("probability is set to ", probability)
print("Tails = 0, Heads = 1: ", fullResults)
#Total up heads and tails for easy user experience 
print("Head Count: ", np.count_nonzero(fullResults == 1))
print("Tail Count: ", np.count_nonzero(fullResults == 0))