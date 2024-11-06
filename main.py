def get_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter not in char_dict:
                    char_dict[letter] = 1
                else:
                    char_dict[letter] += 1
    return char_dict

def sort_char(char_dict):
    return dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))

def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")

    book = get_book(book_path)
    word_counts = count_words(book)
    print(f"{word_counts} words found in the document\n")

    char_dict = sort_char(count_characters(book))
    for letter, count in char_dict.items():
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")


frankenstein_path = "books/frankenstein.txt"

print_report(frankenstein_path)

