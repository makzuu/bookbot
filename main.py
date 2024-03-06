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

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    words_count = count_words(file_contents)
    print(f"words: {words_count}")

    letters_count = count_letters(file_contents)
    print(letters_count)

main()
