import sys
from stats import get_num_words, get_char_occurence, get_sorted_dicts
import os
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = os.path.join(os.path.dirname(__file__), sys.argv[1])
    num_words = get_num_words(filepath)
    dict = get_char_occurence(filepath)
    sorted = get_sorted_dicts(dict)

    alpha_pairs = [(pair["char"], pair["num"]) for pair in sorted if pair["char"].isalpha()]

    formatted_lines = "\n".join(f"{ch}: {cnt}" for ch, cnt in alpha_pairs)
    
    print(f"""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n\n----------- Word Count ----------\nFound {num_words} total words\n\n--------- Character Count -------\n{formatted_lines}\n============= END ===============\n """
    )

main()