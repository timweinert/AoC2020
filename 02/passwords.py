def split_data(pw):
    return pw.split(":")


def validator(raw_pw):
    (pol, pw) = split_data(raw_pw)
    pw = pw.strip()
    (mm, char) = pol.split()
    (charmin, charmax) = mm.split("-")
    charmin = int(charmin) - 1
    charmax = int(charmax) - 1

    if (pw[charmin] == char) ^ (pw[charmax] == char):
        return 1
    else:
        return 0


def main():
    data = open("input.txt", "r").read().split("\n")
    valid_pw = map(validator, data)
    print(sum(valid_pw))


if __name__ == "__main__":
    main()


def test_validator():
    assert validator("1-3 a: abcde") == 1
    assert validator("1-3 b: cdefg") == 0
    assert validator("2-9 c: ccccccccc") == 0
