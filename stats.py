def get_num_words(text):
    # Count words by splitting the text and getting the length
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Convert all text to lowercase
    text = text.lower()
    
    # Count each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count


def sort_chars(char_dict):
    # Create a list to hold dictionaries of characters and counts
    chars_list = []
    
    # Convert the dictionary to a list of dictionaries
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Define a helper function for sorting
    def sort_on(dict):
        return dict["count"]  # We're sorting by "count" instead of "num"
    
    # Sort the list by count (from highest to lowest)
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list




