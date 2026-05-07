def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    from collections import Counter
    bag = Counter('rothes')
    words = load_words()
    results = sorted(w for w in words if len(w) == 6 and not (Counter(w) - bag))
    print(results)
