from flask import Flask, request
from markov import MarkovChain
from histogram import generate_histogram
from histogram import get_unique_words
from sample_freqs import weight_sum
from random import randint
from credentials import *
import tweepy
app = Flask(__name__)
print(tweepy.__version__)

@app.route('/')
def generate_words():
  markov = MarkovChain(["one", 'fish', "two", "fish", "red", "fish", "blue", "fish"])
  return markov.walk(5) 



 

if __name__ == "__main__":
  app.run()
  
          
