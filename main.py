import sys
from stats import get_num_words, get_char_count, sort_chars

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    file_contents = get_book_text(path)
    
    # Get word count
    word_count = get_num_words(file_contents)
    
    # Get character counts
    char_count = get_char_count(file_contents)
    
    # Sort the character counts
    sorted_chars = sort_chars(char_count)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each alphabetical character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

# Call main function
if __name__ == '__main__':
    main()