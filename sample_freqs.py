from histogram import generate_histogram
from random import *
import sys
histogram = {'one': 1, 'fish': 4, 'two': 1, 'red':1, 'blue': 1}

def weight_sum(histogram):
    sum = 0
    range = 0

    for word in histogram.keys():
        sum+=histogram[word]
        
        
    rand_index = randint(0,sum )

    for word, value in histogram.items():
        range += value
        print(range)
        if rand_index <= range:
            return word


if __name__ == "__main__":
    i=0
    l = {}
    while i < 1000:
        w = weight_sum(histogram)
        l[w] = l.get(w, 0) + 1
        i+=1

    print(l)
    
