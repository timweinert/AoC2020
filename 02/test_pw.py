from passwords import validator


def test_validator():
    assert validator("1-3 a: abcde") == 1
    assert validator("1-3 b: cdefg") == 0
    assert validator("2-9 c: ccccccccc") == 0
