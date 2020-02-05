from flask import Flask
from histogram import generate_histogram
from histogram import get_unique_words
app = Flask(__name__)

@app.route('/')
def generate_words():
    lines = get_lines("./words.txt")
    my_histogram = histogram
    sentance = ""

    num_words = 10
    for i in range(num_words):
      word = weighted_sample(my_histogram)