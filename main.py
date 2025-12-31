#main.py
import sys
from stats import count_words, count_chars, sort_dict_list, sort_on

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file):
    return file.read() #return file as string
    
def main(filepath):
    with open(filepath) as f:
        text = get_book_text(f)
    num_words = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = sort_dict_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count --------")
    for char_dict in sorted_char_count:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main(sys.argv[1])





# Alternative way to print:
'''def main(filepath):
    with open(filepath) as f:
        text = get_book_text(f)
    num_words = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = sort_dict_list(char_count)
    
    char_lines = "\n".join([f"{char_dict['char']}: {char_dict['num']}" for char_dict in sorted_char_count])
    
    output = f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{char_lines}
============= END ==============="""
    
    print(output)'''