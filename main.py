# Function that returns an integer value of the word count of its input.
def count_words(words):
    word_array = words.split()
    word_count = len(word_array)
    return word_count

# Function that returns a sorted dictionary (greatest->least) with each character in the input string
# and the amount of times it was counted inside that string.
def count_characters(words):
    # count all characters and place them inside a dict {word:count}
    data = words.lower()
    characters = "abcdefghijklmnopqrstuvwxyz"
    dict = {}
    for character in data:
        if character in characters:
            if character in dict:
                dict[character] += 1
            else:
                dict[character] = 1
    # Sort dict from greatest occurance to least
    sorted_values = sorted(dict.values(), reverse=True)
    sorted_dict = {}
    for value in sorted_values:
        for keys in dict.keys():
            if dict[keys] == value:
                sorted_dict[keys] = value
    return sorted_dict

def main():
    argument = "books/frankenstein.txt"
    with open(argument) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        characters = count_characters(file_contents)
        print(f"-- Begin report of {argument} ---")
        print(f"{word_count} words found in the document")
        print()
        for key,value in characters.items():
            print(f"The letter \'{key}\' character was found {value} times")
        print("--- End report ---")
main()