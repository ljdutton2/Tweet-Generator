from flask import Flask, request
from histogram import generate_histogram
from histogram import get_unique_words
from sample_freqs import weight_sum
from random import randint
app = Flask(__name__)

@app.route('/')
def generate_words():
    histogram = generate_histogram("one fish two fish red fish blue fish")
    print(histogram)
    #num = request.args.get(str("number"))

    sentence = ""
    for i in range(0,10):
      word = weight_sum(histogram)
      sentence += " " + word
    return sentence

if __name__ == "__main__":
  app.run()
  
          
