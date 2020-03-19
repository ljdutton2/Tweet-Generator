from dictogram import Dictogram
from flask import Flask, request
from markov import MarkovChain
from histogram import generate_histogram
from histogram import get_unique_words
from sample_freqs import weight_sum
from random import randint
from credentials import *
import tweepy
import re
app = Flask(__name__)



def generate_words(word_num):
  
  with open('test.txt', "r") as file:
    words_list = []
    words = file.read().split()
    for word in words:
         words_list.append(word)
  dictogram = Dictogram(words_list)
  chain = MarkovChain(words_list)
  sentence = ""
  

  for i in range(word_num):
    
    word = dictogram.sample()
    sentence += " " + word
  #sentence = chain.walk(word_num) 
  return sentence
  return chain.walk(word_num)

  

@app.route('/')
def index():
  return generate_words(9)
 

if __name__ == "__main__":
  app.run()
  
          
