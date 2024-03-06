def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters_count = {}
    for letter in text:
        if letter.isalpha():
            lower = letter.lower()
            if lower in letters_count:
                letters_count[lower] += 1
            else:
                letters_count[lower] = 1
    return letters_count

def sort_on(dict):
    return dict["count"]

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    words_count = count_words(file_contents)

    letters_count = count_letters(file_contents)
    letters_count_list = []
    for letter in letters_count:
        letters_count_list.append({ "letter": letter, "count": letters_count[letter] })
    letters_count_list.sort(key=sort_on, reverse=True)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_count} words found in the document")
    for dict in letters_count_list:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")
    print("--- End report ---")

main()
