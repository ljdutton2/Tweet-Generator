from histogram import generate_histogram
import random
import sys

def weight_sum(histogram):
    sum = 0

    for word in histogram:

        sum+=histogram[word]
    return sum



def gen_rand_word(text):

    text_histo = generate_histogram(text)

    random_weight = random.randint(0,int(weight_sum(text_histo)))
    

    for key, value in text_histo.items():

        random_weight = random_weight - value


        if random_weight <= 0:

            gen_word = key

            return gen_word

        else:

            continue

if __name__ == "__main__":

    test_file = sys.argv[1]

    gen_word = gen_rand_word(test_file)

    print(gen_word)
