from operator import itemgetter
from collections import namedtuple
from typing import List

TestCase = namedtuple("TestCase", ["size", "matrix", "clicks_amount", "clicks_order"])


def main():
    case_count = int(input())

    test_cases: List[TestCase] = []

    for i in range(case_count):
        empty = input()
        size = [int(x) for x in input().split()]
        matrix = []
        for _ in range(size[0]):
            row = [int(x) for x in input().split()]
            matrix.append(row)
        clicks_amount = int(input())
        clicks_order = [int(x) for x in input().split()]

        test_cases.append(TestCase(size, matrix, clicks_amount, clicks_order))
    for test in test_cases:
        for click in test.clicks_order:
            test.matrix.sort(key=itemgetter(click - 1))
        for row in test.matrix:
            print(" ".join(map(str, row)))
        print()


if __name__ == "__main__":
    main()
