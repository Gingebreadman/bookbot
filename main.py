def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    from stats import get_num_words, count_chars, sorted_char_count
    num = get_num_words(text)
    char_counts = count_chars(text)
    sorted_dict = sorted_char_count(char_counts)




    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")




def get_book_text(path):
    with open(path) as f:
        return f.read()



main()












