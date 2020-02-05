from histogram import generate_histogram
from random import *
import sys
text = ''
histogram = {'one': 1, 'fish': 4, 'two': 1, 'red':1, 'blue': 1}

def weight_sum(histogram):
    sum = 0
    start = 0
    end = 0

    for word in histogram.keys():
        sum+=histogram[word]
        
        
    rand_index = randint(0,sum -1)

    for word, value in histogram.items():
        end = start + value

        if rand_index in range(start + end):
            return word
        else:
            start = end
    
i=0
while i < 1000:
   
    print(weight_sum(histogram))
    i+=1

