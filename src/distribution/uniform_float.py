import random
"""
get 'count' uniformly distributed values in in min to max
"""

def uniform_float(min, max , count  ):
    set = []
    
    dist = max - min

    for i in range(count) :
        val = min + dist*random.random()
        set.append(val)

    return set
