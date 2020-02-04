

def generate_histogram(text):
    with open(text, "r") as file:
        og_text = file.read()
    word_list = og_text.split()
    for index, word in enumerate(word_list):
        word_list[index] = word.rstrip("&#@+?/[]{}!:;*_-.,()<>'")
    histogram = {}
    for word in word_list:
        word = word.rstrip()
        if word in histogram.keys():
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

def get_unique_words(histogram):
    unique_words = []
    for word in histogram:
        if histogram[word] == 1:
            unique_words.append(word)
    return unique_words





if __name__ == "__main__":
    text = "test.txt"
    histo = generate_histogram(text)
    print(histo)
