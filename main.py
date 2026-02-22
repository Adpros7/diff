sample_input: str = """abcddef vdfaddwf
friends afraid
delicious indiginous
shalom saaalaaam
happy shipshape
"""
def main(input: str = sample_input):
    words = [sorted(v.split(maxsplit=1), key=len) for v in input.split("\n")]
    for i, v in enumerate(words):
        if len(v[0]) != len(v[1]):
            words[i][1] = words[i][1][:len(v[0])]


    return words


if __name__ == "__main__":
    print(main())
