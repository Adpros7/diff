sample_input: str = """abcddef vdfaddwf
friends afraid
delicious indiginous
shalom saaalaaam
happy shipshape"""

ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"


def sort_by_alphabet(s: str) -> int:
    return ALPHABET.find(s)


def main(input: str = sample_input):
    words: list[list] = [sorted(v.split(), key=len) for v in input.split("\n")]

    for i, v in enumerate(words):
        if len(v[0]) != len(v[1]):
            words[i][1] = words[i][1][: len(v[0])]

    for i in words:
        for x, y in zip(i[0], i[1]):
            pass
        
    return words


if __name__ == "__main__":
    print(main())
