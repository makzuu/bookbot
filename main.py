def count_words(text):
    words = text.split()
    return len(words)

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    words_count = count_words(file_contents)
    print(f"words: {words_count}")

main()
