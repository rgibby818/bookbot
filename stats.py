# Function that returns an integer value of the word count of its input.
def count_words(words):
    word_array = words.split()
    word_count = len(word_array)
    return word_count
