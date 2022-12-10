def load_words():
    with open("words_alpha.txt") as word_file:
        return set(word_file.read().split())

if __name__ == '__main__':
    english_words = load_words()
    print("Ctrl+C to exit")
    try:
        while True:
            print(input("Check word validity > ") in english_words)
    except (KeyboardInterrupt, EOFError):
        exit()
