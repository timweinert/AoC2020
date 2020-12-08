import math
from itertools import combinations


def main():
    data = open("input.txt", "r").read().split("\n")
    expenses = list(map(int, data))

    comb = combinations(expenses, 3)
    filter_function = filter(lambda x: sum(x) == 2020, comb)
    valid_combination = list(filter_function)
    print(math.prod(valid_combination[0]))


if __name__ == "__main__":
    main()