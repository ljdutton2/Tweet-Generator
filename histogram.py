#text = "Step 1: Gather the ingredients and preheat the oven It is essential to use butter, eggs, and milk that are at room temperature. Room temperature ingredients will combine more easily, giving you a properly emulsified batter. Set the butter, eggs, and milk out on the counter 1 hour before you plan to make the cake. Measure out all the other ingredients and have them ready to use. Prepare your stand mixer with the paddle attachment or handheld mixer with beaters. Lightly grease and flour two 9-inch round cake pans and line the bottoms with parchment paper. Preheat the oven about 30 minutes before you begin making the batter. Step 2: Cream the butter and sugar together The butter must be room temperature in order for it to cream properly with the sugars. This is why it is so important to set it out 1 hour ahead of time. Use a stand mixer fitted with the paddle attachment to beat the butter and sugar together. You’re looking for a light and fluffy texture. It should appear lighter in color and double the sized in volume once it has been creamed properly. This can take 5 to 10 minutes."
#words = text.split()
#print(words)


def generate_histogram(words):
    histogram = {}
    words = words.split()
    for word in words:
        
        if word in histogram.keys():
            histogram[word] = histogram[word] + 1
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
    histogram = generate_histogram(words)
    unique_words = get_unique_words(histogram)

    print('--WORD FREQUENCIES--')
    print(histogram)
    print('--UNIQUE WORDS--')
    print(unique_words)