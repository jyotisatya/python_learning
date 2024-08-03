import argparse


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Count occurrences of specific words in a given string.")
    parser.add_argument('word_count', type=str, help="Comma-separated list of words to count.")

    # Parse arguments
    args = parser.parse_args()

    # Convert comma-separated list of words into a list
    word_count = [word.strip() for word in args.word_count.split(',')]

    # Hardcoded input string
    input_string = """the game of thorne is the best serial and I like this season very much, A man is strong with 
    his will and a sword is the ! mighty with its sharpness, is is A special game is sth where you can play hard and fast and that is the ultimate 
    game"""

    # Initialize dictionary
    word_dict = {word: 0 for word in word_count}

    # Process the input string
    input_array = input_string.split()

    for item in input_array:
        new_item = clean_item(item).lower()

        if new_item in word_dict:
            word_dict[new_item] += 1
    
    print(word_dict)

if __name__ == "__main__":
    main()
