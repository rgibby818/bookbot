import sys
from stats import count_words
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
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    argument = sys.argv[1] 
    with open(argument) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        characters = count_characters(file_contents)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {argument} ---")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for key,value in characters.items():
            print(f"{key}: {value}")
        print("--- End report ---")
main()
