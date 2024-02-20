def main():
    path = "books/frankenstein.txt"
    contents = get_book(path)
    words = count_words(contents)
    letter_count = count_letters(contents)
    report = print_report(letter_count)

    print(f"--- Begin report of {path} ---")
    print(f"{words} found in the document")
    for key in report:
        k = key["key"]
        v = key["num"]
        print(f"The '{k}' character was found {v} times")
    print("--- End Report ---")


def count_words(file_contents):
    words = file_contents.split()
    return len(words)


def count_letters(contents):
    letters = {}
    lowered = contents.lower()
    for c in lowered:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1
    return letters


def get_book(path):
    with open(path) as f:
        return f.read()


def print_report(dict):
    counts = []
    for key in dict:
        if key.isalpha():
            counts.append({"key": key, "num": dict[key]})
    counts.sort(reverse=True, key=sort_on)
    return counts


def sort_on(dict):
    return dict["num"]


main()
