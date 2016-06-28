import random
"""
get 'count' uniformly distributed values in in min to max
"""

def uniform_int(min, max , count  ):
    set = []

    for i in range(count) :
        val = random.randint(min , max )
        set.append(val)

    return set
